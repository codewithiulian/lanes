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
    [(319, height), (982, height), (554, 258)]], dtype = np.int32)
    mask = np.zeros_like(image, dtype = np.uint8)
    cv2.fillPoly(mask, polygons, (255,255,255))
    masked_image = cv2.bitwise_and(mask, image)
    return masked_image

lane_image = np.copy(image)
canny = canny(lane_image)
masked_image = region_of_interest(image)
cv2.imshow("result", masked_image)
cv2.waitKey(0)
