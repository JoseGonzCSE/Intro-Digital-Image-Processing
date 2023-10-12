
from PIL import Image,ImageOps

import numpy as np
from numpy import asarray
#sets boundry
rows=100
cols=256

#create numpy matrix with values above
im_pixels=np.zeros(shape=(rows,cols))

#creates a gradient grayscale of image
for i in range(rows):
    count=0
    for j in range(cols):
        im_pixels[i][j]=count
        count=count+1

#open image and show
im_T3=Image.fromarray(np.uint8(im_pixels))
im_T3.show()

#compute avg pixel value
n_pixels=cols*rows
pixels=0
for i in  range(rows):
    for j in range(cols):
        pixels=pixels+im_pixels[i][j]

avgPix=pixels/n_pixels
print("The average value is ",avgPix)
#save as tif
im_T3.save("Task3.tif")

