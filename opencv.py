# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:34:50 2021

@author: Lokesh Rudraradhya
"""

import cv2

img=cv2.imread("C:\\Users\\Lokesh\\Downloads\\HithashreeTL.jpeg",1)
#img=cv2.imread("C:\\Users\\AG07256\\Downloads\\HithashreeTL.jpeg",0)
#print(img)
#print(type(img))
#print(img.shape)
#resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
resized_image=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
cv2.imshow("Legend",resized_image)
cv2.waitKey()
cv2.destroyAllWindows()







