import numpy as np
import cv2

img = cv2.imread('practice/3.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
tem = cv2.imread('practice/4.jpg', 0)
tem = cv2.resize(tem, (0, 0), fx=0.5, fy=0.5)
h, w = tem.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
        cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    res = cv2.matchTemplate(img2, tem, method) 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location  = min_loc
    else:
        location = max_loc
    
    bottom_right_loc = (location[0]+w, location[1]+h )
    cv2.rectangle(img2, location, bottom_right_loc, 255, 10)
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
