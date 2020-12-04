import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

def make_coordinates(image, line_parameters):
    # Deconstruct the slope and y-intercept passed in
    slope, intercept = line_parameters
    # y1 is the first element of the shape prop array (img height)
    y1 = image.shape[0]
    # both of the lines will start from the bottom of the image and go up
    # 3 5ths towards the middle of the image
    y2 = int(y1*3/5)
    # define x => y = mx + b <=> x = (y - b) / m
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

"""
Returns the average slope and y-intercept.
The Slope is the letter m and the y-intercept is the letter b from the formula:
y = mx + b
m = (y2 - y1) / (x2 - x1) => meaning the vertical change over the horizontal one
b = y - mx
"""
def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        # Decompose the points of each line.
        x1, y1, x2, y2 = line.reshape(4)
        """
        numpy.polifit returns a fits the polynomial y = mx + b to the given
        coordinates, and return a vector of coeficients, that describe the slope
        and y-intercept (m and b)
        arg1: x coordinates of the two points
        arg2: y coordinates of the two points
        arg3: polynomial degree
        """
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        # Get the Slope & y-intercept which is the first element in the array
        # of format: [slope y-intercept] or [m b] i.e. [   1. -286.]
        slope, intercept = parameters[0], parameters[1]
        # If the slope is negative
        if slope < 0:
            # Means it's the left lane line
            left_fit.append([slope, intercept])
        else:
            # If positive, it means it's the right lane line
            right_fit.append([slope, intercept])
    # Average up the values of slope and y-intercept
    # Do this vertically on the first axis (y)
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    # Define the left and right line coordinates
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    return np.array([left_line, right_line])

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny;

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
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
canny_image = canny(lane_image)
cropped_image = region_of_interest(canny_image)
hough_lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]),
minLineLength=40, maxLineGap=5)
averaged_lines = average_slope_intercept(lane_image, hough_lines)
line_image = display_lines(lane_image, averaged_lines)
final_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
cv2.imshow("result", final_image)
cv2.waitKey(0)
