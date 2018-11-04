#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:08:59 2018

@author: Tarek M. Sayed
@Email: atamish@gmail.com
"""
import numpy as np
import cv2
# read image
img = cv2.imread("opencv_logo.png")
# set wendow opject
cv2.namedWindow("opencv logo", cv2.WINDOW_NORMAL)
# show image
cv2.imshow("opencv logo", img)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
