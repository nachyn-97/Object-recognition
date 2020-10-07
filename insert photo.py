import cv2
import numpy as np

img1 = cv2.imread("img1.png")
img2 = cv2.imread("img2.png")

img1 = cv2.resize(img1, (50, 50))
img2 = cv2.resize(img2, (300, 300))

dst_top_corner_position = (20, 60)
height, width, _ = img1.shape
x1, y1 = dst_top_corner_position
x2, y2 = x1 + width, y1 + height

gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, threshed = cv2.threshold(gray_img1, 10, 255, cv2.THRESH_BINARY)
ret, reversed_threshed = cv2.threshold(gray_img1, 10, 255, cv2.THRESH_BINARY_INV)

foreground = cv2.bitwise_and(img1, img1, mask=threshed)

reversed_threshed = cv2.cvtColor(reversed_threshed, cv2.COLOR_GRAY2BGR)
background = img2.copy()[y1:y2, x1:x2, :]
background = cv2.bitwise_and(background, reversed_threshed)

overlay_result = cv2.bitwise_or(background, foreground)

dst_img = img2.copy()
dst_img[y1: y2, x1:x2] = overlay_result

cv2.imshow("dst_img", dst_img)
cv2.waitKey()
cv2.destroyAllWindows()