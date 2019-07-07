#!/usr/bin/env python
# -*- coding: UTF-8
from PIL import Image
from tkinter import filedialog
import cv2
import tkinter
import pdb
"""
    Util that crops a selected Image and Saves it
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


class Cropper:

    def crop_image(self, path):
        crop_coords = []
        cropping_mode = False
        img = None
        try:
            def click_and_crop(event, x, y, flags, param):
                nonlocal crop_coords, cropping_mode

                if event == cv2.EVENT_LBUTTONDOWN and not cropping_mode:
                    if len(crop_coords) == 2:
                        remove_rec(crop_coords)
                    crop_coords = [(x, y)]
                    cropping_mode = True
                elif event == cv2.EVENT_LBUTTONUP:
                    crop_coords.append((x, y))
                    cropping_mode = False
                    cv2.rectangle(
                        img,
                        crop_coords[0],
                        crop_coords[1],
                        (0, 255, 0),
                        0
                    )

                    imagePil = Image.open(path)
                    img_matrix = imagePil.load()
                    newImg = Image.new(
                        imagePil.mode,
                        (
                            (crop_coords[1][0] - crop_coords[0][0]),
                            (crop_coords[1][1] - crop_coords[0][1])
                        )
                    )
                    x = 0
                    for i in range(crop_coords[0][0], crop_coords[1][0]):
                        y = 0
                        for j in range(crop_coords[0][1], crop_coords[1][1]):
                            r = img_matrix[i, j][0]
                            g = img_matrix[i, j][1]
                            b = img_matrix[i, j][2]
                            gray = (r+g+b) // 3
                            newImg.putpixel((x, y), (gray, gray, gray))
                            y = y + 1
                        x = x + 1
                    newImg.save("./img/cropped.png", imagePil.format)

            img = cv2.imread(path)
            img = cv2.resize(img, (400, 400))
            clone = img.copy()

            cv2.namedWindow('Crop Your Image')
            cv2.setMouseCallback("Crop Your Image", click_and_crop)

            while True:
                cv2.imshow('Crop Your Image', img)
                key = cv2.waitKey(1) & 0xFF

                if key == ord('r'):
                    img = clone.copy()
                elif key == ord('c'):
                    break
            cv2.destroyAllWindows()
        except:
            print('You didn\'t choose an Image')
