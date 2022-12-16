import numpy as np
import cv2

img = cv2.imread('practice/2.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_img, 50, 0.01, 10)
corners = np.int0(corners)

for cor in corners:
    x, y = cor.ravel()
    cv2.circle(img, (x, y), 5, (0,0,255), -1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        cor1 = tuple(corners[i][0])
        cor2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
        cv2.line(img, cor1, cor2, color, 1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
