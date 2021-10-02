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
        self.input_textbox = tk.Text(frame, height=1.5, width=20)

        self.input_textbox.place(x=275, y=450)

        # Button Creation
        printButton = tk.Button(frame, text="Confirm", command=self.read_input)
        printButton.place(x=330, y=500)

        # Cue label Creation
        self.cue_label = tk.Label(frame, text="", font=("Helvetica bold", 13))
        self.cue_label.place(x=225, y=50)

        # Image label Creation
        self.image_label = tk.Label(frame, text="")
        self.image_label.place(x=180, y=130)

        first_fact = self.model.get_next_fact(current_time=0)
        self.display_cue(first_fact[0])

        frame.mainloop()

    def display_text(self, fact_text: str) -> None:
        self.cue_label.config(text=fact_text)

    def display_image(self, img_file: str) -> None:
        image = Image.open(img_file)
        image = image.resize((350, 280), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)

        self.image_label.image = image_tk
        self.image_label.config(image=image_tk)

    def display_cue(self, fact) -> None:
        # print(fact)
        if fact.question_type == "Phylum":
            self.display_text("What phylum are these families?")
        if fact.question_type == "Family":
            self.display_text("What family are these genuses?")
        if fact.question_type == "Genus":
            self.display_text("What genus are these species?")
        else:
            self.display_text("What species is shown below?")
            self.display_image(fact[2])

    def read_input(self) -> str:
        input_text = self.input_textbox.get(1.0, "end-1c")

        return input_text
