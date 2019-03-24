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
        icon = Image.open('./img/icon.png')
        icon = ImageTk.PhotoImage(icon)
        self.window_container.tk.call('wm', 'iconphoto', self.window_container._w, icon)
        self.window_container.title('Cheetah Detection')
        self.set_background()
        self.center_window()

    def center_window(self):
        self.window_container.update_idletasks()
        w = self.window_container.winfo_width()
        h = self.window_container.winfo_height()
        x = (self.window_container.winfo_screenwidth() // 2) - (w // 2)
        y = (self.window_container.winfo_screenheight() // 2) - (h // 2)
        self.window_container.geometry('{}x{}+{}+{}'.format(w, h, x, y))

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
