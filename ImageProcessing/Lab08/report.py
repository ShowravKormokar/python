#Bit plane slicing & image reconstruction
import PIL.Image as image
import matplotlib.pyplot as plt
import numpy as np

#a) Read a grayscale image
img = image.open('doller.webp').convert('L')
img_arr = np.array(img)

bit_planes = []
#b) bit plane slicing to extract all 8 bit planes (0–7) using the expression
for k in range(8):
    plane = (img_arr >> k) & 1
    bit_planes.append(plane) # c) Store all the bit planes into an array.  

plt.figure(figsize=(20,4))
#d) Display all extracted bit planes in a 2 × 4 grid 
#with appropriate titles (Bit Plane 0 to Bit Plane 7).  
for k in range(8):
    plt.subplot(2,4,k+1)
    plt.imshow(bit_planes[k], cmap='gray')
    plt.title(f"Bit Plane {k}")
    plt.axis("off")
plt.show()

recon = np.zeros_like(img_arr)
#e) Reconstruct a new image using only the higher-order bit planes
for k in range(4,8):
    recon = recon + bit_planes[k] * (2**k)

plt.figure(figsize=(20,5))
#f) Display both the original image and the reconstructed image
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(recon, cmap='gray')
plt.title('Reconstructed Imgae (4-7)')
plt.axis('off')
plt.show()