import cv2 # OpenCV
import numpy as np

# Save the input image into a multidimensional array
image = cv2.imread('test_image.jpg')
# Make a copy of the image array
# This is necessary as we don't want to make changes to the
# original array.
lane_image = np.copy(image)
# Now converting to grayscale
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

cv2.imshow('result', gray) # Show the image using OpenCV
# This function is necessary for showing the display window
cv2.waitKey(0) # The argument is the milliseconds, 0 is infinite
