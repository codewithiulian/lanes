import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny;

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]], dtype = np.int32)
    mask = np.zeros_like(image, dtype = np.uint8)
    print(mask)
    cv2.fillPoly(mask, polygons, (255,255,255))
    masked_image = cv2.bitwise_and(mask, image)
    return masked_image

lane_image = np.copy(image)
canny = canny(lane_image)
cropped_image = region_of_interest(canny)
"""
Draws the Hough lines
arg1: the image cropped
arg2: the bin size that collect votes on the number of lines intersections
based on the number of points detected in the cartesian space
arg3: precision in degrees: one degree to radians = pi/180 = 1
arg4: lower threshold: the minimum number of intersections needed to
detect the line
arg5: placeholder array to be passed in
arg6: the lenght of the line in px accepted in the output
arg6: max line gap: the maximum distance in px between segmented lines
which we'll allow to be connected into a single one.
"""
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLenght=40, maxLineGap=5)
cv2.imshow("result", cropped_image)
cv2.waitKey(0)
