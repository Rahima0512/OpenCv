#BASIC FUNCTIONS
import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
#GET IMAGE IN GRAY IMAGE:
img= cv2.imread("model.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
#GET IMAGE IN BLUR IMAGE:
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)
#GET EDGES OF THE IMAGE:
imgCanny=cv2.Canny(img,150,200)
cv2.imshow("Canny Image",imgCanny)
#GET EDGES OF THE IMAGE BROADER:
imgDialation=cv2.dilate(imgCanny,kernel,iterations=2)
cv2.imshow("Dialated Image",imgDialation)
#GET EDGES OF THE IMAGE BROADER:
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
