#!/usr/bin/env python
from pathlib import Path
from tkinter import Tk
from tkinter import Label, Button, StringVar, Canvas, Frame, filedialog
from PIL import Image, ImageTk
import pdb
import os
"""
    GUI Class Manager that initalizes the actual window
"""
_author__ = 'Jose Epifanio'
__credits__ = [
    'Ludim Sanchez',
    'Alberto Hernandez',
    'Guillermo Gonzalez',
    'Jose Epifanio'
]
__licence__ = 'MIT'
__version__ = '1.0.0'
__email__ = 'jose.epifanio90@gmail.com'
__status__ = 'Development'


class GuiManager():
    def __init__(self):
        self.window = Tk()

    def init_view(self):
        self.set_main_container()
        self.window.mainloop()

    def set_main_container(self):
        icon = Image.open('./img/icon.png')
        icon = ImageTk.PhotoImage(icon)
        self.window.tk.call('wm', 'iconphoto', self.window._w, icon)  # noqa
        self.window.title('Cheetah Detection')
        self.center_window()
        self.set_ui()

    def center_window(self):
        self.window.update_idletasks()
        w, h = 1200, 350
        x = (self.window.winfo_screenwidth() // 2) - (w // 2)
        y = (self.window.winfo_screenheight() // 2) - (h // 2)
        self.window.geometry(f'{w}x{h}+{x}+{y}')

    def set_ui(self):
        self.add_frames()
        self.add_label_titles()
        self.add_img_frames()
        self.add_buttons()

    def add_frames(self):
        self.header_frame = Frame(self.window)
        self.header_frame.pack(side='top', fill='both')
        self.left_frame = Frame(self.window)
        self.left_frame.pack(side='left', fill='both', padx=65)
        self.right_frame = Frame(self.window)
        self.right_frame.pack(side='right', fill='both', padx=55)
        self.btm_frame = Frame(self.window)
        self.btm_frame.pack(side='bottom', fill='both')

    def add_label_titles(self):
        usr_lbl_title = StringVar()
        usr_lbl = Label(
            self.header_frame,
            textvariable=usr_lbl_title,
            relief='flat'
        )
        usr_lbl_title.set('Your selected Image')
        usr_lbl.pack(side='left', fill='both', padx=220)

        out_lbl_title = StringVar()
        out_lbl = Label(
            self.header_frame,
            textvariable=out_lbl_title,
            relief='flat'
        )
        out_lbl_title.set('Output Image')
        out_lbl.pack(side='right', fill='both', padx=220)

    def add_img_frames(self):
        usr_canva = Canvas(self.left_frame, bg='red', relief='raised')
        usr_canva.pack(fill='both', padx=20, pady=50)

        out_canva = Canvas(
            self.right_frame,
            bg='blue',
            relief='raised'
        )
        out_canva.pack(fill='both', padx=20, pady=50)

    def add_buttons(self):
        load_btn = Button(self.btm_frame, text='Load Image',
                          command=self.btn_callback)
        load_btn.pack(side='left', padx=25)
        snip_btn = Button(self.btm_frame, text='Snip Image',
                          command=self.btn_callback)
        snip_btn.pack(side='left', padx=25)
        start_btn = Button(self.btm_frame, text='Start!',
                           command=self.btn_callback)
        start_btn.pack(side='left', padx=25)
        cls_btn = Button(self.btm_frame, text='Clear',
                         command=self.btn_callback)
        cls_btn.pack(side='left', padx=25)

    def btn_callback(self):
        image_file = filedialog.askopenfile(initialdir=os.getcwd(), filetypes=(
            ("JPEG", ".jpg"), ("PNG", ".png"), ("All Files", "*.*")))
        image = ImageTk.PhotoImage(Image.open(image_file.name))
