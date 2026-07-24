import cv2

# Read grayscale image
img = cv2.imread("image.jpg", 0)

# Histogram Equalization
equal = cv2.equalizeHist(img)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equal)

cv2.waitKey(0)
cv2.destroyAllWindows()
