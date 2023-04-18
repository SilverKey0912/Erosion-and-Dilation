import cv2
import matplotlib
import numpy

# Read the image for erosion
img1 = cv2.imread("/content/wire.tif", 0)
# Acquire size of the image
m, n = img1.shape
# Show the image
plt.imshow(img1, cmap="gray")
# Define the structuring element
# k= 11,15,45 -Different sizes of the structuring element
k = 15
SE = np.ones((k, k), dtype=np.uint8)
constant = (k - 1) // 2
# Define new image
imgErode = np.zeros((m, n), dtype=np.uint8)
# Erosion without using inbuilt cv2 function for morphology
for i in range(constant, m - constant):
    for j in range(constant, n - constant):
        temp = img1[i - constant:i + constant + 1, j - constant:j + constant + 1]
        product = temp * SE
        imgErode[i, j] = np.min(product)
        cv2.imshow("old.png", img1)

cv2.imshow("Eroded.png", imgErode)
plt.imshow(imgErode, cmap="gray")
cv2.imwrite("Eroded3.png", imgErode)
