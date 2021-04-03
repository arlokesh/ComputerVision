# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:34:50 2021

@author: Lokesh Rudraradhya
"""

import cv2
face_cascade=cv2.CascadeClassifier("C:\\worked\\Data_science\\ML-Deployment\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img=cv2.imread("C:\\Users\\Lokesh\\Downloads\\HithashreeTL.jpeg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()