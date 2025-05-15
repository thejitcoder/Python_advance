# Uploading image using python

import matplotlib.pyplot as plt
import matplotlib.image as img

testimage = img.imread('v.jpeg')

print("Before showing image")
plt.imshow(testimage)
plt.axis('off')  # Optional: hides axis ticks
plt.show()
print("After showing image")