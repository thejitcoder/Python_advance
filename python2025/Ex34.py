# pip install OpenCV
import cv2 
import matplotlib.pyplot as plt 
  
# read image 
image = cv2.imread('h.jpeg') 

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
# call imshow() using plt object 
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()
  
# display that image 

img1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image

plt.imshow(img1, cmap= "gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
 