from tkinter import *
import tkinter as tk
from spacingmodel import *

class app():

	def __init__(self, name, height, width):
		window = tk.Tk()
		window.title(name)
		# Width, height in pixels
		frame=Frame(window, height = height, width = width)
		frame.pack()
		window.mainloop()

	def insert_text(self):
		pass

	def insert_image(self):
		pass

	def display_cue(self):
		self.insert_text()
		self.insert_image()
		pass

	def read_input(self):
		pass


test = app("Name", 500, 500)