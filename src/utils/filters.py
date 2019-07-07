#!/usr/bin/env python
# -*- coding: UTF-8
from PIL import Image
import numpy as np
import cv2
'''
    Util that contains all the used filters in the app
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


class Filters:
    # def __init__(self, image):
    #     self.img = image

    def apply_filters(self, sides):
        for side in sides:
            print('Applying Filters...')
            image = cv2.imread(f'./img/cropped{side}.png')
            gaussian = cv2.GaussianBlur(image, (5, 5), 0)
            cv2.imwrite(f'./img/gaussian{side}.png', gaussian)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'./img/gray{side}.png', gray)
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)
            cv2.imwrite(f'./img/laplacian{side}.png', laplacian)
            print(f'Applied All Filters for side {side}...')

    def grayScale(self):
        for x in range(self.width):
            for y in range(self.heigth):
                red, blue, green = self.img.getpixel((x, y))
                gray = int(0.21 * red + 0.72 * green + 0.07 * blue)
                self.img.putpixel((x, y), (gray, gray, gray))
        self.img.save('./img/cheetahGray2.png', self.img.format)
        print('GrayScale Done...')

    def fourBitThreshold(self):
        print('Starting threshold')
        ran = 255 // 4
        for x in range(self.width):
            for y in range(self.heigth):
                gray = self.img.getpixel((x, y))
                gray = gray[0]
                if gray > 0 and gray < ran:
                    if(ran/2) > gray:
                        gray = 0
                    else:
                        gray = ran
                elif gray > ran and gray < (ran * 2):
                    if((ran * 2) // 2) > gray:
                        gray = ran
                    else:
                        gray = ran * 2
                elif gray > (ran * 2) and gray < (ran * 3):
                    if((ran * 3) // 2) > gray:
                        gray = ran * 2
                    else:
                        gray = ran * 3
                elif gray > (ran * 3) and gray < (ran * 4):
                    if ((ran * 4) // 2) > gray:
                        gray = ran * 3
                    else:
                        gray = ran * 4
                else:
                    gray = 255
                self.img.putpixel((x, y), (gray, gray, gray))
        self.img.save('./img/cheetahFourBitThreshold.png', self.img.format)
        print('Four Bit Threshold Done...')

    def filterBefore(self):
        print('Applying some bilateral Filter.')
        img = cv2.imread('./img/cheetahGray2.png')
        bilateral = cv2.bilateralFilter(img, 9, 75, 75)
        cv2.imwrite('./img/cheetahBilateralFilterBefore.png', bilateral)
        print('Bilateral Filter Done.')

    def secondTime(self):
        print('Applying some bilateral Filter.')
        img = cv2.imread('./img/cheetahGaussian.png')
        bilateral = cv2.bilateralFilter(img, 9, 75, 75)
        bilateral = cv2.medianBlur(bilateral, 7)
        bilateral = cv2.GaussianBlur(bilateral, (5, 5), 0)
        blur = cv2.GaussianBlur(bilateral, (5, 5), 0)
        cv2.imwrite('./img/cheetahSecondTime.png', bilateral)
        print('Bilateral Filter Done.')

    def bilateralFilter(self):
        print('Applying some bilateral Filter.')
        img = cv2.imread('./img/cheetahFourBitThreshold.png')
        bilateral = cv2.bilateralFilter(img, 9, 75, 75)
        bilateral = cv2.medianBlur(bilateral, 3)
        bilateral = cv2.GaussianBlur(bilateral, (5, 5), 0)
        blur = cv2.GaussianBlur(bilateral, (5, 5), 0)
        cv2.imwrite('./img/cheetahGaussian.png', bilateral)
        print('Bilateral Filter Done.')

    def circlesDetection(self):
        print('Detecting Circles')
        img = cv2.imread('./img/cheetahGaussian.png', 0)
        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        circles = cv2.HoughCircles(
            img,
            cv2.cv.CV_HOUGH_GRADIENT,
            1,
            20,
            param1=50,
            param2=30,
            minRadius=0,
            maxRadius=0
        )
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv2.imwrite('./img/detected circles.png', cimg)
        print('Circles detection Done.')
