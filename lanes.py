import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny;

def region_of_interest(image):
    # height is the first axis from the shape property
    height = image.shape[0]
    polygons = np.array([
    [(319, height), # point B
    (982, height), # point C
    (554, 258)] # point A
    ], dtype = np.int32)
    # draw a mask of the same shape as the image
    mask = np.zeros_like(image, dtype = np.uint8) # zeros is color black
    # fill the polygon with our triangle, bg color of white
    cv2.fillPoly(mask, polygons, (255,255,255))
    return mask

lane_image = np.copy(image)
canny = canny(lane_image)
mask = region_of_interest(image)
cv2.imshow("result", mask)
cv2.waitKey(0)
