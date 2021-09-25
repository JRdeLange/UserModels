from tkinter import *
import tkinter as tk
from spacingmodel import *
from PIL import ImageTk, Image


class app():

	def __init__(self, name, width, height):
		# Top level window
		frame = tk.Tk()
		frame.title("TextBox Input")
		frame.geometry(f'{width}x{height}')

		# Function for getting Input
		# from textbox and printing it
		# at label widget

		# TextBox Creation
		self.input_textbox = tk.Text(frame, height=1.5, width=20)

		self.input_textbox.place(x=275, y=450)

		# Button Creation
		printButton = tk.Button(frame,
								text="Confirm",
								command=self.read_input)
		printButton.place(x=330, y=500)

		# Cue label Creation
		self.cue_label = tk.Label(frame, text="", font=("Helvetica bold", 13))
		self.cue_label.place(x=195, y=50)

		# Image label Creation
		self.image_label = tk.Label(frame, text="")
		self.image_label.place(x=180, y=130)

		if self.cue_label.cget("text") == "":
			self.display_cue(["What is the species of the animal below?", "kitten.jpg"])

		frame.mainloop()

	def display_text(self, fact_text: str) -> None:
		self.cue_label.config(text=fact_text)

	def display_image(self, img_file: str) -> None:
		print(img_file)
		image = Image.open(img_file)
		print(image)
		image = image.resize((350, 280), Image.ANTIALIAS)
		image_tk = ImageTk.PhotoImage(image)

		self.image_label.image = image_tk
		self.image_label.config(image=image_tk)

	def display_cue(self, fact) -> None:
		#print(fact)
		self.display_text(fact[0])
		self.display_image(fact[1])

	def read_input(self) -> str:
		input_text = self.input_textbox.get(1.0, "end-1c")

		return input_text


test = app("Name", 700, 550)
