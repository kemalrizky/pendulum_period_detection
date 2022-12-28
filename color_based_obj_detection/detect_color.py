import cv2 
import numpy as np

video = cv2.VideoCapture("image path")
success, img = video.read()

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Hue Min","HSV",0,179,empty)
cv2.createTrackbar("Hue Max","HSV",179,179,empty)
cv2.createTrackbar("Sat Min","HSV",0,255,empty)
cv2.createTrackbar("Sat Max","HSV",255,255,empty)
cv2.createTrackbar("Value Min","HSV",0,255,empty)
cv2.createTrackbar("Value Max","HSV",255,255,empty)


while True:
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos("Hue Min","HSV")
    hmax = cv2.getTrackbarPos("Hue Max","HSV")
    smin = cv2.getTrackbarPos("Sat Min", "HSV")
    smax = cv2.getTrackbarPos("Sat Max", "HSV")
    vmin = cv2.getTrackbarPos("Value Min", "HSV")
    vmax = cv2.getTrackbarPos("Value Max", "HSV")

    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax, smax, vmax])
    mask = cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    stackedImg = np.hstack([img,result,mask])

    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.imshow("Result", stackedImg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
