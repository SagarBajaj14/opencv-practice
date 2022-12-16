import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    width = int(cap.get(3)) # 3rd property of videocapture is width
    height = int(cap.get(4))  # 4th property of videocapture is height
    
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10)
    img = cv2.rectangle(img, (100, 100), (200, 200), (150, 190, 200), -1)
    img  = cv2.circle(img, (200, 200), 50, (0,0,255), 5)
    text = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'OpenCV practice', (100,height-100), text, 2,(0,0,0), 10, cv2.LINE_AA)

    cv2.imshow('frame', img)

    #press q to quit
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()