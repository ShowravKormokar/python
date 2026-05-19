# ================================
# Lab-7: Gray Level Slicing
# ================================

import PIL.Image as image
import matplotlib.pyplot as plt
import numpy as np

# 1. Read a grayscale image
gray_img = image.open("hand_xray.jpg").convert('L')

# Convert image to numpy array
img = np.array(gray_img)

# Display original image
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')
plt.show()


# ==========================================
# Define gray-level range
# ==========================================

A = 100
B = 180


# ==========================================
# Gray-Level Slicing with Background Preserved
# If A <= r <= B, then s = 255
# Otherwise, keep original pixel value
# ==========================================

slice_with_bg = np.copy(img)

H, W = img.shape

for i in range(H):
    for j in range(W):

        # Check pixel range
        if A <= img[i, j] <= B:
            slice_with_bg[i, j] = 255
        else:
            slice_with_bg[i, j] = img[i, j]


# ==========================================
# Gray-Level Slicing without Background
# If A <= r <= B, then s = 220
# Otherwise, s = 0
# ==========================================

slice_without_bg = np.zeros_like(img)

for i in range(H):
    for j in range(W):

        # Check pixel range
        if A <= img[i, j] <= B:
            slice_without_bg[i, j] = 220
        else:
            slice_without_bg[i, j] = 0


# ==========================================
# Display all images
# ==========================================

plt.figure(figsize=(18, 6))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# With background preserved
plt.subplot(1, 3, 2)
plt.imshow(slice_with_bg, cmap='gray')
plt.title("Gray Level Slicing\nWith Background")
plt.axis('off')

# Without background
plt.subplot(1, 3, 3)
plt.imshow(slice_without_bg, cmap='gray')
plt.title("Gray Level Slicing\nWithout Background")
plt.axis('off')

plt.show()