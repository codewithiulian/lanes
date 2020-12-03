import cv2 # OpenCV
import numpy as np

image = cv2.imread('test_image.jpg')

lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
"""
Apply Canny edge detection. Pass in a threshold of
1:3. Meaning the differences in color intensity lower
than 50, is ignored (and therefore rendered as black).
And the differences above 150 are considered edges And
rendered as white.
"""
canny = cv2.Canny(blur, 50, 150)

cv2.imshow('result', canny)
cv2.waitKey(0)
