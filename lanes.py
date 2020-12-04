import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny;

def display_lines(image, lines):
    line_image = np.zeros_like(image) # draw a black background
    if lines is not None: # if there are any Hough lines detected
        for line in lines: # iterate though each of them
            """
            Note: each line in lines is a 2D array reshape turns it into a 1D
            array or better yet, for each line, save the coordinates into their
            respective variables.
            """
            x1, y1, x2, y2 = line.reshape(4)
            """
            Use the coordinates to draw the line.
            arg1: the background
            arg2: Starting point of the line segment (x and y coordinates)
            arg3: Ending point of the line segment (x and y coordinates)
            arg4: Line color
            arg5: Line thickness
            """
            cv2.line(line_image, (x1, y1), (x2, y2), (255 , 0, 0), 10)
    return line_image

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]], dtype = np.int32)
    mask = np.zeros_like(image, dtype = np.uint8)
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
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(lane_image, lines)
cv2.imshow("result", line_image)
cv2.waitKey(0)
