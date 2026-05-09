import numpy as np
import PIL.Image as image
import matplotlib.pyplot as plt

img = image.open('einstein.jpeg').convert('L')
img_array = np.array(img)

# a) Compute frequency of each intensity level.
hist = np.zeros(256, dtype=int)

pixels = img_array.flatten()

for i in pixels:
    hist[i] += 1

plt.bar(range(256), hist)
plt.title("Histogram (Frequency)")
plt.xlabel("Intensity")
plt.ylabel("Count")
plt.show()

# b) Calculate probability density function (PDF). 
total_pixels = img_array.size

pdf = np.zeros(256, dtype=float)

for i in range(256):
    pdf[i] = hist[i]/total_pixels

# c) Calculate cumulative distribution function (CDF).
cdf = np.zeros(256, dtype=float)
cdf[0] = pdf[0]

for i in range(1, 256):
    cdf[i] = cdf[i-1] + pdf[i]

# d) Map old pixel values to new values.
new_level = np.zeros(256, dtype=int)
new_level = np.round(255 * cdf) 


equalized_img = np.zeros_like(img_array)

H, W = img_array.shape

for i in range(H):
    for j in range(W):
        equalized_img[i, j] = new_level[img_array[i, j]]

plt.imshow(equalized_img, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')
plt.show()

hist = np.zeros(256, dtype=int)
pixels = equalized_img.flatten()

for i in pixels:
    hist[i] += 1

plt.bar(range(256), hist)
plt.title("Histogram (Frequency)")
plt.xlabel("Intensity")
plt.ylabel("Count")
plt.show()