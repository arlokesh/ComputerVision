# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:34:50 2021

@author: Lokesh Rudraradhya
"""

import cv2,time,pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
	check,frame=video.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray=cv2.GaussianBlur(gray,(21,21),0)

	if first_frame is None:
		first_frame = gray
		continue
	delta_frame=cv2.absdiff(first_frame,gray)
	thresh_delta=cv2.threshold(delta_frame,30,224,cv2.THRESH_BINARY)[1]
	thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)
	(cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	for contour in cnts:
		if cv2.contourArea(contour)<1000:
			continue

		(x,y,w,h)=cv2.boundingRect(contour)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

	cv2.imshow('frame',frame)
	cv2.imshow('capturing',gray)
	cv2.imshow('delta',delta_frame)
	cv2.imshow('thresh',thresh_delta)

	key=cv2.waitKey(1)
	if key==ord('q'):
		break
video.release()
cv2.destroyAllWindows()

