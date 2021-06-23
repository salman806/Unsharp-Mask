
"""
unsharp mask

unsharpend image = orginal + amount*(orginal - blured)
"""
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
from matplotlib import pyplot as plt

img = img_as_float(io.imread('C:/Users/DELL/Desktop/hopfield/f.png',as_gray=True))

gaussian_img = gaussian(img , sigma=2, mode='constant',cval=0.0)

img2 = (img - gaussian_img)*2 

img3 = img + img2

plt.imshow(img3,cmap="gray")



