import cv2

# Read image
img = cv2.imread("image.jpg")

# Rotate image 90° clockwise
rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
