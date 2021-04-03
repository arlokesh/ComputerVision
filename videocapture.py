# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:34:50 2021

@author: Lokesh Rudraradhya
"""

import cv2,time
video= cv2.VideoCapture(0,cv2.CAP_DSHOW)
check,frame=video.read()
print(check)
print(frame)
time.sleep(10)
cv2.imshow('Capture',frame)
cv2.waitKey()
video.release()
cv2.destroyAllWindows()
