import cv2
import matplotlib
import numpy

# Read the image for dilation
img2 = cv2.imread("/content/text.tif", 0)
# Acquire size of the image
p, q = img2.shape
# Show the image
plt.imshow(img2, cmap="gray")
# Define new image to store the pixels of dilated image
imgDilate = np.zeros((p, q), dtype=np.uint8)
# Define the structuring element
SED = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
constant1 = 1
# Dilation operation without using inbuilt CV2 function
for i in range(constant1, p - constant1):
    for j in range(constant1, q - constant1):
        temp = img2[i - constant1:i + constant1 + 1, j - constant1:j + constant1 + 1]
        product = temp * SED
        imgDilate[i, j] = np.max(product)
plt.imshow(imgDilate, cmap="gray")
cv2.imshow("old.png", img2)
cv2.imshow("Dilated.png", imgDilate)
cv2.imwrite("Dilated.png", imgDilate)
