import cv2
import random

image = cv2.imread("newimg.jpg", 1)

#print(img) displays the pixels in numpy array
#print(img.shape) rows,columns and bgr values used to represent pixels
for i in range(100):
    for j in range(image.shape[1]):
        image[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To copy and paste a part of image
#var = img[row1:row2, col1:col2]
#img[finalrow1:finalrow2, finalcol1:finalcol2] = var