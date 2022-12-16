import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    width = int(cap.get(3)) # 3rd property of videocapture is width
    height = int(cap.get(4))  # 4th property of videocapture is height

    #Converting BGR to HSV color pallete
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Defining bounds of color to be captured
    light_blue = np.array([90, 50, 50])
    dark_blue = np.array([130,255,255])

    #Masking to get only defined color range
    mask = cv2.inRange(hsv, light_blue, dark_blue)

    #Compares original and masked image to output result
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', res)
    cv2.imshow('mask', mask)

    #press q to quit
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()