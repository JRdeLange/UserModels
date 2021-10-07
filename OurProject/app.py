from tkinter import *
from spacingmodel import *

import tkinter as tk
from PIL import ImageTk, Image
import time


class App:
    def __init__(self, name, width, height, fact_dict, tree_dict, learned_dict, model):

        # vars
        self.fact_dict = fact_dict
        self.tree_dict = tree_dict
        self.learned_dict = learned_dict
        self.model = model
        self.width = width
        self.height = height

        # Top level window
        frame = tk.Tk()
        frame.title(name)
        frame.geometry(f"{width}x{height}")

        # Function for getting Input
        # from textbox and printing it
        # at label widget

        # TextBox Creation
        self.input_textbox = tk.Text(frame, height=1.5, width=51)

        self.input_textbox.place(x=width / 4, y=450)

        # Button Creation
        self.Button = tk.Button(frame, text="Confirm", command=self.press_button)
        self.Button.place(x=330, y=500)

        # Cue label Creation
        self.cue_label = tk.Label(frame, text="", font=("Helvetica bold", 16))
        self.cue_label.place(x=225, y=50)

        # Q example label Creation
        self.q_examples_label = tk.Label(frame, text="", font=("Helvetica bold", 13))

        # Answer label Creation
        self.answer_label = tk.Label(frame, text="", font=("Helvetica bold", 13))
        self.answer_label.place(x=230, y=420)

        # Image label Creation
        self.image_label = tk.Label(frame, text="")

        # time stuff
        self.app_start_time = time.time() * 1000
        self.fact_start_time = 0
        self.response_time = 0
        print("fact start time: ", self.fact_start_time)
        # display first fact
        self.current_fact, self.current_new = self.model.get_next_fact(current_time=self.fact_start_time)
        self.display_cue(self.current_fact)

        frame.mainloop()

    def display_question(self, fact_text: str) -> None:
        self.cue_label.config(text=fact_text)

    def display_q_examples(self, examples: str) -> None:
        text = examples.replace(",", "\n")
        self.q_examples_label.config(text=text)
        self.q_examples_label.place(x=225, y=80)

    def display_answer(self, answer_text: str) -> None:
        self.answer_label.config(text=answer_text)

    def display_image(self, img_file: str) -> None:
        image = Image.open(img_file)
        image = image.resize((350, 280), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)

        self.image_label.image = image_tk
        self.image_label.config(image=image_tk)
        self.image_label.place(x=175, y=110)

    def display_cue(self, fact) -> None:
        if fact.question_type == "Phylum":
            self.display_question("What phylum are these families?")
            self.image_label.place_forget()
            self.display_q_examples(fact.question)
        elif fact.question_type == "Family":
            self.display_question("What family are these genuses?")
            self.image_label.place_forget()
            self.display_q_examples(fact.question)
        elif fact.question_type == "Genus":
            self.display_question("What genus are these species?")
            self.image_label.place_forget()
            self.display_q_examples(fact.question)
        else:
            self.display_question("What species is shown below?")
            self.q_examples_label.place_forget()
            self.display_image(fact[2])
        # If it is the first time the fact has been encountered, then the answer is also shown
        if self.current_new:
            text = "Answer: " + fact.answer
            self.display_answer(text)
        else:
            text = ""
            self.display_answer(text)

    def press_button(self) -> None:
        if self.Button['text'] == "Confirm":  # response given
            self.response_time = (time.time() * 1000) - self.fact_start_time - self.app_start_time  # record response time
            print("response time: ", self.response_time)
            input_text = self.input_textbox.get(1.0, "end-1c")  # retrieve given response
            self.process_response(input_text)
            self.input_textbox.delete("1.0", "end")
            self.input_textbox.place_forget()

        elif self.Button['text'] == "Next":  # start of next fact shown
            self.fact_start_time = (time.time() * 1000) - self.app_start_time  # get current time for when the fact is shown
            print("fact start time: ", self.fact_start_time)
            self.current_fact, self.current_new = self.model.get_next_fact(current_time=self.fact_start_time)  # get new fact
            self.display_cue(self.current_fact)  # display new fact
            self.input_textbox.place(x=self.width / 4, y=450)  # place textbox
            self.Button['text'] = "Confirm"

    def process_response(self, output):
        correct = self.simplify_str(output) == self.simplify_str(inp=self.current_fact.answer)
        response = Response(self.current_fact, start_time=self.fact_start_time, rt=self.response_time, correct=correct)
        self.model.register_response(response)
        self.update_learned(correct)
        self.Button['text'] = "Next"

    def update_learned(self, correct):
        if not self.current_new and correct:  # increase the number of correct responses
            self.learned_dict[self.current_fact] += 1

        if not correct:  # reset the counter for responses
            self.learned_dict[self.current_fact] = 0

        for category in self.tree_dict:  # go through the parents
            add = True
            for item in self.tree_dict[category]:  # go through the children of each parent
                if self.learned_dict[self.fact_dict[item]] < 2:  # TODO: decide on a threshold for learned
                    add = False
            if add and self.fact_dict[category] not in self.model.facts:  # make sure the fact hasn't already been added
                self.model.add_fact(self.fact_dict[category])

        if correct:
            self.display_answer("That's correct!")
        else:
            text = "Wrong, the answer is: " + self.current_fact.answer
            self.display_answer(text)

    @staticmethod
    def simplify_str(inp: str) -> str:
        trans_table = inp.maketrans("-", " ")
        inp = inp.translate(trans_table).lower()
        return inp
