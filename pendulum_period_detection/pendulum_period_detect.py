import cv2
import numpy as np

# Initialization
cap = cv2.VideoCapture(r"C:\Users\User\Projects\KSIC\UTS\pendulum loop.mp4")
frame_width = 240
frame_height = 180
cap.set(3,frame_width)
cap.set(4,frame_height)

epsilon = 1
i = 0
init_centroid = []
stop = False

while True:
    success, img = cap.read() 
    
    # Image Preprocessing
    # convert the BGR image to HSV colour space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # set the bounds for the red hue
    lower_red = np.array([0,64,154])
    upper_red = np.array([179,255,255])
    # create a mask using the bounds set
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Processing
    # Determining center of mass
    M = cv2.moments(mask)
    cX = round(int(M["m10"] / M["m00"]))
    cY = round(int(M["m01"] / M["m00"]))
    centroid = (cX,cY)
    area = M["m00"]

    cv2.circle(img, centroid, 3, (0,255,0), -1)

    # store initial centroid position
    if i == 0:
        init_centroid.append(centroid[0])
        init_centroid.append(centroid[1])
        init_area = area
        t_start = cv2.getTickCount()
        T = 0
    
    # get the period if centroid reaches initial position
    if (i > 10 and stop == False and abs(centroid[0]-init_centroid[0]) <= epsilon and abs(centroid[1]-init_centroid[1]) <= epsilon and area-init_area < epsilon):
        
        T = round((cv2.getTickCount() - t_start)/cv2.getTickFrequency(),2)
        stop = True
        print("Oscillation Period =",T)
    
    t = round((cv2.getTickCount()-t_start)/cv2.getTickFrequency(), 2)
    i = i + 1

    # Display time and period
    cv2.putText(img,("t = "+str(t)+" s"),(75,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,100,0),2)
    cv2.putText(img,("Period = "+str(T)+" s"),(75,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,100,0),2)
    
    # Display the image
    cv2.imshow("Result Image", img)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    wait = int((1/fps)*1000-15)
    if cv2.waitKey(wait) & 0xFF == ord('q'):
        break