import cv2

# Read image
img = cv2.imread("image.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
