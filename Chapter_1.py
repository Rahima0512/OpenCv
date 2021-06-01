#READ-IMAGES-VIDEOS-WEBCAM
import cv2
#READ IMAGE
img= cv2.imread("lambo.jpg")
cv2.imshow("Image",img)
cv2.waitKey(0)

#TO CAPTURE VIDEO:
cap=cv2.VideoCapture("Pexels Videos 1494279.mp4")
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break

#TO USE WEBCAM:
cap = cv2.VideoCapture(0)
cap.set(3,640)     #3- width id number
cap.set(4,480)     #4- height id number
cap.set(10,100)    #3- brightness id number

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break


