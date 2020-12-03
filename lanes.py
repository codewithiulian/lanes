import cv2 # OpenCV
import numpy as np

# Save the input image into a multidimensional array
image = cv2.imread('test_image.jpg')

cv2.imshow('result', image) # Show the image using OpenCV
# This function is necessary for showing the display window
cv2.waitKey(0) # The argument is the milliseconds, 0 is infinite
