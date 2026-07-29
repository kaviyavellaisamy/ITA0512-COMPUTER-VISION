import cv2

# Read image
img = cv2.imread("image.jpg")

# Resize image
small = cv2.resize(img, (300, 200))
large = cv2.resize(img, (900, 700))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image", small)
cv2.imshow("Larger Image", large)

cv2.waitKey(0)
cv2.destroyAllWindows()
