import cv2

# Read image
img = cv2.imread("image.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
