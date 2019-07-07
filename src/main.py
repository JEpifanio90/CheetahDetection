#!/usr/bin/env python
# -*- coding: UTF-8
from gui.gui_manager import GuiManager
'''Simple Image Classification. A bare bone Machine Learning implementation.

Essentially this is going to compare two images and remove their colors
by applying all sorts of filters. Next with the help of KNN and other
algorithms we are going to calculate a percentage of similitude and
display it to the user.

NOTE: Everything was made without TensorFlow or any other ML/DL
libraries
'''
__author__ = 'Jose Epifanio'
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


class Main():
    def __init__(self):
        pass

    def start(self):
        guiManager = GuiManager()
        guiManager.init_view()


if __name__ == '__main__':
    main_instance = Main()
    main_instance.start()
