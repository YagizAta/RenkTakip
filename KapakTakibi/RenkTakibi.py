
import cv2 as cv
import numpy as  np


res = np.array((400,400,1),np.uint8)

def fonk(sayi):
    print(sayi)


cv.namedWindow("Trackbar")
cv.createTrackbar("AzM","Trackbar",0,255,fonk)
cv.createTrackbar("CokM","Trackbar",0,255,fonk)
cv.createTrackbar("AzY","Trackbar",0,255,fonk)
cv.createTrackbar("CokY","Trackbar",0,255,fonk)
cv.createTrackbar("AzK","Trackbar",0,255,fonk)
cv.createTrackbar("CokK","Trackbar",0,255,fonk)

takip = cv.VideoCapture("takip.mp4")

while True:
    cv.imshow("Trackbar",res)
    kontrol,yakala = takip.read()
    azM=cv.getTrackbarPos("AzM","Trackbar")
    cokM=cv.getTrackbarPos("CokM","Trackbar")
    azY=cv.getTrackbarPos("AzY","Trackbar")
    cokY=cv.getTrackbarPos("CokY","Trackbar")
    azK=cv.getTrackbarPos("AzK","Trackbar")
    cokK=cv.getTrackbarPos("CokK","Trackbar")


    az = np.array([azK,azY,azM])
    cok = np.array([cokK,cokY,cokM])
    istenen = cv.inRange(yakala,az,cok)

    son = cv.bitwise_and(yakala,yakala,mask=istenen)
    #cv.imshow("Video",yakala)
    #cv.imshow("İstenen",istenen)
    cv.imshow("Son hal",son)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

    cv.waitKey(1)






