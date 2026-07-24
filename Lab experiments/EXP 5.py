import cv2
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("image.jpg")

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)

plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Number of Pixels")
plt.show()
