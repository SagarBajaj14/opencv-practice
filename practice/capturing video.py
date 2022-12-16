import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    width = int(cap.get(3)) # 3rd property of videocapture is width
    height = int(cap.get(4))  # 4th property of videocapture is height

    img = np.zeros(frame.shape, np.uint8)

    frame_small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    img[:height//2, :width//2] = cv2.rotate(frame_small,cv2.ROTATE_180)#top left
    img[height//2:, :width//2] = frame_small #bottom left
    img[:height//2, width//2:] = frame_small#top right
    img[height//2:, width//2:] = cv2.rotate(frame_small,cv2.ROTATE_180) #bottom right
    


    cv2.imshow('frame', img)

    #press q to quit
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()