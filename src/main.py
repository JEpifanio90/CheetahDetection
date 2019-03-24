#!/usr/bin/env python
from pathlib import Path
from tkinter import Tk
from tkinter import messagebox, Label
from PIL import Image, ImageTk
"""Simple Image Classification. A bare bone Machine Learning implementation.

Some issue alskdalskdl.
"""
__author__ = 'Jose Epifanio'
__credits__ = ['Ludim Sanchez', 'Alberto Hernandez', 'Guillermo Gonzalez']
__licence__ = 'MIT'
__version__ = "1.0.0"
__email__ = "jose.epifanio90@gmail.com"
__status__ = "Development"


class Main():
    def __init__(self):
        self.window_container = Tk()

    def init_view(self):
        self.set_main_container()
        self.window_container.mainloop()

    def set_main_container(self):
        self.window_container.geometry("650x400")
        self.window_container.title('Cheetah Detection')
        self.set_background()

    def set_background(self):
        bg_image = Image.open('./img/background.png')
        bg_image = ImageTk.PhotoImage(bg_image)
        img_background = Label(self.window_container, image=bg_image)
        img_background.image = bg_image
        img_background.pack()
        img_background.grid(row=0, column=0)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.init_view()
