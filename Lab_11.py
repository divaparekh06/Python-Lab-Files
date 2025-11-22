# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# print(img_array)
# y1, x1 = 100, 100  # Top-left corner of ROI
# y2, x2 = 250, 200  # Bottom-right corner of ROI
# cropped_img = img_array[y1:y2, x1:x2]
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array)
# plt.title('Original Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(cropped_img)
# plt.title('Cropped Image')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# rotated_img = np.rot90(img_array)
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array)
# plt.title('Original Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(rotated_img )
# plt.title('Rotated Image (90 degrees)')
# plt.axis('off')

# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# flipped_img = np.fliplr(img_array)
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array)
# plt.title('Original Image')
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.imshow(flipped_img )
# plt.title('Flipped Image')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# is_grayscale = len(img_array.shape) < 3
# # Function to create negative of an image
# def create_negative(image):
#     if is_grayscale:
#         # For grayscale images
#         negative_image = 255 - image
#     else:
#         # For color images (RGB)
#         negative_image = 255 - image
#     return negative_image
# # Create negative of the image
# negative_img = create_negative(img_array)
# # Display the original and negative images
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array)
# plt.title('Original Image')
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.imshow(negative_img)
# plt.title('Negative Image')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image, ImageOps
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# # Binarize the image using a threshold
# threshold = 128
# binary_img = np.where(img_array < threshold, 0, 255).astype(np.uint8)
# # Display the original and binarized images
# plt.figure(figsize= (10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array, cmap='gray')
# plt.title('Original Grayscale Image')
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.imshow(binary_img, cmap='gray')
# plt.title('Binarized Image (Threshold = 128)')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image, ImageOps
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# # Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
# gray_img = np.dot (img_array[..., :3], [0.299, 0.587, 0.114])
# # Display the original RGB image
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_array)
# plt.title('Original RGB Image')
# plt.axis('off')
# # Display the converted grayscale image
# plt.subplot(1, 2, 2)
# plt.imshow(gray_img, cmap='gray')
# plt.title('Grayscale Image')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# import numpy as np
# from PIL import Image, ImageOps
# import matplotlib.pyplot as plt
# img = Image.open(r'C:\Users\Diva Parekh\Downloads\MU lab11.jpg')
# img_array = np.array(img)
# # Compute the histogram of the image
# hist, bins = np.histogram(img_array.flatten(), bins=256, range= (0, 256))
# # Plot the histogram
# plt.figure(figsize=(10, 5))
# plt.hist(img_array.flatten(), bins=256, range= (0, 256), density=True, color='gray')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Normalized Frequency')
# plt.title('Histogram of Grayscale Image')
# plt.grid(True)
# plt.show()




#---------POST LABS-----------
#Question 1
import numpy as np
from PIL import Image

img = Image.open(r"C:\Users\Diva Parekh\Downloads\MU lab11.jpg")
# img_array = np.array(img)
# height, width, channels = img_array.shape
# min_blue = img_array[:, :, 2].min()   
# print(f"Image Dimensions: {img_array.shape}")  
# print(f"Height: {height}, Width: {width}, Channels: {channels}")
# print(f"Minimum pixel value in Blue channel: {min_blue}")

#Question 2
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# img = Image.open(r"C:\Users\Diva Parekh\Downloads\MU lab11.jpg")
# img_array = np.array(img)
# padded_img = np.pad(img_array, ((50, 50), (100, 100), (0, 0)), mode='constant', constant_values=0)
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.imshow(img_array)
# plt.title("Original Image")
# plt.axis("off")
# plt.subplot(1,2,2)
# plt.imshow(padded_img)
# plt.title("Padded Image (Black)")
# plt.axis("off")
# plt.tight_layout()
# plt.show()


#Question 3
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# img = Image.open(r"C:\Users\Diva Parekh\Downloads\MU lab11.jpg")
# img_array = np.array(img)
# R = img_array[:, :, 0]
# G = img_array[:, :, 1]
# B = img_array[:, :, 2]

# plt.figure(figsize=(12,4))
# plt.subplot(1,3,1)
# plt.imshow(R, cmap="Reds")
# plt.title("Red")
# plt.axis("off")
# plt.subplot(1,3,2)
# plt.imshow(G, cmap="Greens")
# plt.title("Green")
# plt.axis("off")
# plt.subplot(1,3,3)
# plt.imshow(B, cmap="Blues")
# plt.title("Blue")
# plt.axis("off")
# plt.tight_layout()
# plt.show()



