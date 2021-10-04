from tkinter import *
from spacingmodel import *

import tkinter as tk
from PIL import ImageTk, Image


class App:
    def __init__(self, name, width, height, fact_dict, tree_dict, model):

        #vars
        self.fact_dict = fact_dict
        self.tree_dict = tree_dict
        self.model = model

        # Top level window
        frame = tk.Tk()
        frame.title(name)
        frame.geometry(f"{width}x{height}")

        # Function for getting Input
        # from textbox and printing it
        # at label widget

        # TextBox Creation
        self.input_textbox = tk.Text(frame, height=1.5, width=51)

        self.input_textbox.place(x=width/4, y=450)

        # Button Creation
        printButton = tk.Button(frame, text="Confirm", command=self.read_input)
        printButton.place(x=330, y=500)

        # Cue label Creation
        self.cue_label = tk.Label(frame, text="", font=("Helvetica bold", 16))
        self.cue_label.place(x=225, y=50)

        # Answer label Creation
        self.answer_label = tk.Label(frame, text="", font=("Helvetica bold", 13))
        self.answer_label.place(x=230, y=420)

        # Image label Creation
        self.image_label = tk.Label(frame, text="")
        self.image_label.place(x=175, y=110)

        self.time = 0  # TODO: make a proper timing thing
        self.current_fact, self.current_new = self.model.get_next_fact(current_time=self.time)
        self.display_cue(self.current_fact)

        frame.mainloop()

    def display_text(self, fact_text: str) -> None:
        self.cue_label.config(text=fact_text)

    def display_answer(self, answer_text: str) -> None:
        self.answer_label.config(text=answer_text)

    def display_image(self, img_file: str) -> None:
        image = Image.open(img_file)
        image = image.resize((350, 280), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)

        self.image_label.image = image_tk
        self.image_label.config(image=image_tk)

    def display_cue(self, fact) -> None:
        if fact.question_type == "Phylum":
            self.display_text("What phylum are these families?")
        if fact.question_type == "Family":
            self.display_text("What family are these genuses?")
        if fact.question_type == "Genus":
            self.display_text("What genus are these species?")
        else:
            self.display_text("What species is shown below?")
            self.display_image(fact[2])
        # If it is the first time the fact has been encountered, then the answer is also shown
        if self.current_new:
            text = "Answer: " + fact.answer
            self.display_answer(text)
        else:
            text = ""
            self.display_answer(text)

    def read_input(self) -> str:
        input_text = self.input_textbox.get(1.0, "end-1c")
        self.process_response(input_text)
        self.display_cue(self.current_fact)
        self.input_textbox.delete("1.0", "end")
        return input_text

    def process_response(self, output):
        # TODO: make it so capitals and dashes wont make things be incorrect
        correct = True if output == self.current_fact.answer else False
        response = Response(self.current_fact, start_time=self.time, rt=2207, correct=correct)  # TODO: timing thing
        self.model.register_response(response)
        self.current_fact, self.current_new = self.model.get_next_fact(current_time=self.time)
        self.time += 3800  # TODO: timing thing

