# Color Processing: Perform operations on a colored image by 
# extracting and manipulating the RGB channels, also converting image to HSV.

# import packagaes for images and arrays
import matplotlib.pyplot as plt
import numpy as numpy
from PIL import Image

# input = "dog.png"

# dog = plt.imread(input) # Read in image from the input
# plt.imshow(dog) # Load image into pyplot
# plt.show() # Show the image

# Single Color Extraction: AI Query - 
# "Extract the Red, Green, and Blue channels from a color image (dog.png). 
# Display each channel as a grayscale image." How to do this via Pillow library in Python?

# dog = Image.open("dog.png").convert("RGB") # Open image, making sure it's in RGB mode

# r, g, b = dog.split() # Split image into RGB channels

# # Show each channel as grayscale image
# r.show(title= "Red Channel")
# g.show(title="Green Channel")
# b.show(title="Blue Channel")

# # Save each grayscale image
# r.save("Red_Dog_GS.png")
# g.save("Green_Dog_GS.png")
# b.save("Blue_Dog_GS.png")

# Color Representation

# Display the channels 

# # False-color images created: merge each channel with other 0 channels
# red_dog = Image.merge("RGB", (r, Image.new("L", r.size), Image.new("L", r.size))) # red false color
# green_dog = Image.merge("RGB", (Image.new("L", r.size), g, Image.new("L", r.size))) # green false color
# blue_dog = Image.merge("RGB", (Image.new("L", r.size), Image.new("L", r.size), b)) # blue false color 

# # Show the false-color images
# red_dog.show(title="Red Channel FC")
# green_dog.show(title ="Green Channel FC")
# blue_dog.show(title="Blue Channel FC")

# # Save the fc images
# red_dog.save("red_dog_fc.png")
# green_dog.save("green_dog_fc.png")
# blue_dog.save("blue_dog_fc.png")

# HSV Channel Extraction

dog_HSV = Image.open("dog.png").convert("HSV") # convert the image to HSV color space

h, s, v = dog_HSV.split() # Split image into HSV channels

# # Show each channel as grayscale image
# h.show(title= "Hue Channel")
# s.show(title="Saturation Channel")
# v.show(title="Value Channel")

# # Save each grayscale HSV image
# h.save("Hue_Dog_GS.png")
# s.save("Sat_Dog_GS.png")
# v.save("Val_Dog_GS.png")

# Saturation Adjustment - AIQuery - How to recombine the adjusted channels?

# sat_array = numpy.array(s, dtype=numpy.float32) # image -> array

# scaling_factors = [0.01, 0.26, 0.46] # scaling factors def

# # diff scaling factors applied
# for factor in scaling_factors:
#     s_scaled = (sat_array * factor).clip(0, 255).astype(numpy.uint8)

#     # recombine w original HV channels
#     new_image = Image.merge("HSV", (h, Image.fromarray(s_scaled), v)).convert("RGB")

#     # Show + save modified images
#     new_image.show(title=f"Dog Saturation Scaled by {factor}")
#     new_image.save(f"dog_saturation_{factor:.2f}.png")





