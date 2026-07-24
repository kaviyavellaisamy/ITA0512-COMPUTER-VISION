import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
erode = cv2.erode(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
