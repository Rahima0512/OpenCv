#shapes and images
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
print(img.shape)
#img[:] = 255,0,0 #to get full image solid filled
#cv2.imshow("Image",img)
#img[200:300,100:300]= 255,0,0 #to fill a proportion
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
"""     (0,0)starting point  img.shape[1] width     img.shape[0] height  
  (0,255,0)   colour     3 thickness   """
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)
"""    (0,0) starting point (250,350) end point  (0,0,255) colour     3 thickness/if you wanna make it solid filled 
use cv2.FILLED"""
cv2.circle(img,(450,50),30,(255,255,0),5)
"""(450,50) center ,30 radius,(255,255,0) colour,5 thickness   """
cv2.putText(img,"OpenCv",(160,450),cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),1)
"""     (160,450) point where to be shown ,cv2.FONT_HERSHEY_COMPLEX font style,
2 size of the written word,(0,150,0) colour,1 thickness    
"""
cv2.imshow("Image",img)
cv2.waitKey(0)