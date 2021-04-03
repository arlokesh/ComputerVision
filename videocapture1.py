# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:34:50 2021

@author: Lokesh Rudraradhya
"""


import cv2,time
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
a=1
while True:
	a=a+1
	check,frame=video.read()
	print(frame)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Capturing',gray)

	key=cv2.waitKey(1)
	if key==ord('q'):
		break
print(a)
video.release()
cv2.destoryAllWindows()