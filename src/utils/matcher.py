#!/usr/bin/env python
# -*- coding: UTF-8
from PIL import Image
from utils.img_utils import ImgUtils
import numpy as np
import cv2
'''
    Util that compares both images
'''
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


class Matcher:

    def compare(self, img, img2):
        image, image2 = Image.open(img), Image.open(img2)
        lista, lista2, dif, dif2 = list(), list(), list(), list()
        width, height = image.size
        act, act2, aciertos, porcentaje, i = 0, 0, 0, 0, 0
        flag = False
        for x in range(width):
            for y in range(height):
                val = image.getpixel((x, y))
                val2 = image2.getpixel((x, y))
                act, act2 = val, val2
                lista.append(val)
                lista2.append(val2)
                if x != 0 and y != 0:
                    u = act-lista[i]
                    o = act2-lista2[i]
                    if u == o:
                        aciertos = aciertos+1
                    porcentaje = (float(aciertos) / float(width * height)) * 100  # nopep8
                    if porcentaje < 38:
                        nuevoPr = float(porcentaje) * 100/38
                    else:
                        nuevoPr = 100
        return '%.2f' % porcentaje
