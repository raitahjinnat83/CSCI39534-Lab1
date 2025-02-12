# Color Processing: Perform operations on a colored image by 
# extracting and manipulating the RGB channels, also converting image to HSV.

# import packagaes for images and arrays
import matplotlib.pyplot as plt
import numpy as numpy
from PIL import Image

input = "dog.png"

# dog = plt.imread(input) # Read in image from the input
# plt.imshow(dog) # Load image into pyplot
# plt.show() # Show the image

# Single Color Extraction

dog = Image.open(input) # Open image

r, g, b = dog.split() # Split image into RGB channels

# Show each channel as grayscale image
r.show(title= "Red Channel")
g.show(title="Green Channel")
b.show(title="Blue Channel")

# Save each grayscale image
r.save("Red_Dog.png")
g.save("Green_Dog.png")
b.save("Blue_Dog.png")



