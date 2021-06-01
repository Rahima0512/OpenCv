#RESIZING AND CROPPING
import cv2
import numpy as np
img=cv2.imread("lambo.jpg")
print(img.shape) #to know the size
imgResize=cv2.resize(img,(300,200)) #(width,height)
imgcropped=img[0:200,200:500]  #(height ,width )
cv2.imshow("Resized image",imgResize)
cv2.imshow("Cropped image",imgcropped)
cv2.waitKey(0)