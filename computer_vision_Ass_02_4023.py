import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from collections import deque
import os


# Create Output Folder

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)


# Assignment 1: Otsu's Thresholding


# Load color image
image = cv2.imread('fruitsample.png')
if image is None:
    print("Error: Image not found.")
    exit()

# Convert for matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.title('Original Image (Color)')
plt.imshow(image_rgb)
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'original_image.png'))
plt.show()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.title('Original Image (Grayscale)')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'original_grayscale.png'))
plt.show()

# Step 2: Add RGB Gaussian Noise
mean = 0
sigma = 80  # Noise level
gaussian_noise_rgb = np.random.normal(mean, sigma, image.shape)
noisy_image = image + gaussian_noise_rgb
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

noisy_image_rgb = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.title('Noisy Image (Color)')
plt.imshow(noisy_image_rgb)
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'noisy_color_image.png'))
plt.show()

# Add noise to grayscale version separately
gaussian_noise_gray = np.random.normal(mean, sigma, gray_image.shape)
noisy_gray_image = gray_image + gaussian_noise_gray
noisy_gray_image = np.clip(noisy_gray_image, 0, 255).astype(np.uint8)

plt.figure()
plt.title('Noisy Image (Grayscale)')
plt.imshow(noisy_gray_image, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'noisy_grayscale_image.png'))
plt.show()

# Step 3: Apply Otsu's Thresholding
threshold = threshold_otsu(noisy_gray_image)
binary_image = (noisy_gray_image > threshold).astype(np.uint8) * 255

plt.figure()
plt.title(f'Otsu Thresholding\nThreshold: {threshold:.2f}')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'otsu_thresholding.png'))
plt.show()


# Assignment 2: Region Growing


# Region Growing Function
def region_growing(image, seed_point, threshold=60):
    visited = np.zeros_like(image, dtype=bool)
    region = np.zeros_like(image, dtype=np.uint8)
    queue = deque()
    queue.append(seed_point)
    seed_value = image[seed_point]
    visited[seed_point] = True

    while queue:
        x, y = queue.popleft()
        region[x, y] = 255

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < image.shape[0]) and (0 <= ny < image.shape[1]) and not visited[nx, ny]:
                    if abs(int(image[nx, ny]) - int(seed_value)) <= threshold:
                        visited[nx, ny] = True
                        queue.append((nx, ny))
    return region

#  Display image to confirm seed selection
plt.figure()
plt.title('Select a Seed Point (click)')
plt.imshow(noisy_gray_image, cmap='gray')
plt.axis('off')

#  Interactive seed selection
coords = plt.ginput(1)
plt.close()

#  Convert coordinates to integer
seed_point = (int(coords[0][1]), int(coords[0][0]))
print(f"Selected seed point: {seed_point}")

# Apply Region Growing
segmented_image = region_growing(noisy_gray_image, seed_point, threshold=50)

plt.figure()
plt.title('Region Growing Result')
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'region_growing_result.png'))
plt.show()

print(f" All images are saved in the '{output_dir}' folder.")
