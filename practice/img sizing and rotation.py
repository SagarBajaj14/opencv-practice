import cv2
import random
import numpy as np

img = cv2.imread("practice/1.jpg", 1)
#image = cv2.resize(img,(400,400))
image = cv2.resize(img,(0,0),fx=0.5,fy=0.5) # another way to manipulate size of the image
image = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE) # rotating values of pixels of image
cv2.imwrite('newimg.jpg', image)  
cv2.imshow('Image', image)
cv2.waitKey(0) # waiting until the user choose to close the window
cv2.destroyAllWindows()
