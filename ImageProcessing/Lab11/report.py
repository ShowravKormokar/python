
# Lab-11: Edge Detection and Image Sharpening
import PIL.Image as image
import numpy as np
import matplotlib.pyplot as plt

# a) Read a grayscale image
gray_img = image.open('./images/cameraman.bmp').convert('L')
# Convert image to numpy array
img = np.array(gray_img)

# Get image height and width
H, W = img.shape
# Display original image
plt.figure(figsize=(10,4))
plt.imshow(gray_img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# b) Use replicate padding (edge padding)
padded_img = np.pad(img, pad_width=1, mode='edge')

# c) Apply a 3×3 Laplacian filter to extract edge image
filter = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

# Create empty array for edge image
laplacian_edges = np.zeros_like(img, dtype=float)

# Apply Laplacian filter using convolution
for i in range(H):
    for j in range(W):
        # Extract 3x3 region
        region = padded_img[i:i+3, j:j+3]
        # Multiply region with filter and sum
        laplacian_edges[i, j] = np.sum(region * filter)

# d) Generate sharpened image using Laplacian output
sharpen_image = img - laplacian_edges

# Clip pixel values and convert to uint8
laplacian_edges = np.clip(laplacian_edges, 0, 255).astype(np.uint8)
sharpen_image = np.clip(sharpen_image, 0, 255).astype(np.uint8)

# e) Display: original image, Laplacian edge image, and sharpened image
plt.figure(figsize=(12,4))

# Original Image
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Laplacian Edge Image
plt.subplot(1,3,2)
plt.imshow(laplacian_edges, cmap='gray')
plt.title("Laplacian Edges")
plt.axis('off')

# Sharpened Image
plt.subplot(1,3,3)
plt.imshow(sharpen_image, cmap='gray')
plt.title("Sharp Image")
plt.axis('off')

plt.tight_layout()
plt.show()

# f) Apply Sobel filter in horizontal direction (Gx)
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

# g) Apply Sobel filter in vertical direction (Gy)
sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

# Create empty arrays
gx = np.zeros_like(img, dtype=float)
gy = np.zeros_like(img, dtype=float)
gradient_magnitude = np.zeros_like(img, dtype=float)

# Padding for Sobel operation
padded_img = np.pad(img, pad_width=1, mode='constant', constant_values=0)

# Apply Sobel filters
for i in range(H):
    for j in range(W):
        # Extract 3x3 region
        region = padded_img[i:i+3, j:j+3]
        # Horizontal edge detection
        gx[i, j] = np.sum(region * sobel_x)
        # Vertical edge detection
        gy[i, j] = np.sum(region * sobel_y)

# h) Compute gradient magnitude using Sobel outputs
gradient_magnitude = np.sqrt(gx**2 + gy**2)

# Convert values into valid image range
gx = np.clip(np.abs(gx), 0, 255).astype(np.uint8)
gy = np.clip(np.abs(gy), 0, 255).astype(np.uint8)
gradient_magnitude = np.clip(gradient_magnitude, 0, 255).astype(np.uint8)

#Display original image, Sobel outputs, and gradient magnitude
plt.figure(figsize=(12,4))

# Original Image
plt.subplot(1,4,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Sobel Horizontal Output
plt.subplot(1,4,2)
plt.imshow(gx, cmap='gray')
plt.title("Sobel Edges (Gx)")
plt.axis('off')

# Sobel Vertical Output
plt.subplot(1,4,3)
plt.imshow(gy, cmap='gray')
plt.title("Sobel Edges (Gy)")
plt.axis('off')

# Gradient Magnitude Image
plt.subplot(1,4,4)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title("Gradient Magnitude")
plt.axis('off')

plt.tight_layout()
plt.show()