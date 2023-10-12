from PIL import Image,ImageOps

import numpy as np
from numpy import asarray

#opens watertower
im=Image.open('Watertower.tif')
#checks if greyscale
print("image mode is:",im.mode)
#shows image
im.show()

#numpy matrix with pixel values

im_pixels=asarray(im)

#imports function
from MyImageFunctions import myImageInverse
#calls function
im_inv_pixels=myImageInverse(im_pixels)
#creates image from inv_pixels
im_inv=Image.fromarray(np.uint8(im_inv_pixels))
#show inverse
im_inv.show()
#save image
im_inv.save("Watertower_inv.tif")



