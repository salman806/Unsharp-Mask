"""
unsharp mask 
unsharp mask only created by one line 
"""

from skimage import io
from skimage.filters import unsharp_mask
from matplotlib import pyplot as plt

img = io.imread('C:/Users/DELL/Desktop/hopfield/f.png')

unsharp_img = unsharp_mask(img, radius=3, amount=3) # radius define the amount of blurring 
plt.imshow(unsharp_img)