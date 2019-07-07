#!/usr/bin/env python
# -*- coding: UTF-8
from pathlib import Path
from PIL import ImageTk, Image
from tkinter import Tk
from tkinter import Label, Button, StringVar, Canvas, Frame, filedialog
from utils.Cropper import Cropper
import PIL
import cv2
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
        self.usr_imgs = {
            'left': None,
            'right': None
        }

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
        usr_lbl.pack(side='left', fill='both', padx=200)

        out_lbl_title = StringVar()
        out_lbl = Label(
            self.header_frame,
            textvariable=out_lbl_title,
            relief='flat'
        )
        out_lbl_title.set('Output Image')
        out_lbl.pack(side='right', fill='both', padx=200)

    def add_img_frames(self):
        self.left_canvas = Canvas(self.left_frame, bg='green', relief='raised')
        self.left_canvas.pack(fill='both')

        self.right_canvas = Canvas(
            self.right_frame,
            bg='blue',
            relief='raised'
        )
        self.right_canvas.pack(fill='both')

    def add_buttons(self):
        self.start_btn = Button(
            self.btm_frame,
            state='disabled',
            text='Start!',
            command=self.btn_callback
        )
        self.start_btn.pack(fill='both', pady='20')
        self.load_btn = Button(
            self.btm_frame,
            text='Load Image',
            command=self.btn_callback
        )
        self.load_btn.pack(fill='both', pady='20')

    def btn_callback(self):
        image_file = filedialog.askopenfile(
            initialdir=os.getcwd(),
            filetypes=(
                ("All Files", "*.*"),
                ("GIF", ".jpg"),
                ("JPEG", ".jpg"),
                ("PNG", ".png"),
            )
        )
        self.process_image(image_file)

    def process_image(self, image_path):
        cropper = Cropper()
        base_width = 600
        cropper.crop_image(image_path.name)
        image = Image.open('./img/cropped.png')
        height = image.height * (base_width // image.width)
        image = image.resize((base_width, height), PIL.Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.usr_imgs['left'] = image
        self.left_canvas.create_image(
            image.width() // 2,
            image.height() // 2,
            image=self.usr_imgs['left']
        )
        self.load_btn['state'] = 'disabled'
        self.start_btn['state'] = 'normal'
