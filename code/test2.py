import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('pic1.jpg',0)
print(img)

#cv2.imwrite('pic1-grey.jpg',img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
