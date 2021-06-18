import cv2
import numpy as np
img=cv2.imread("Cards.jpg")

width,height=791,1007
pts1=np.float32([[177,337],[787,237],[943,1127],[325,1237]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("Output",imgOut)

cv2.waitKey(0)