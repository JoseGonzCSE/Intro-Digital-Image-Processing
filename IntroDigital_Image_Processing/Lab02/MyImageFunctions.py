from PIL import Image,ImageOps

import numpy as np
from numpy import asarray

#will inverse image
def myImageInverse(inImage):
    #determines size of inImage
    rows, cols = inImage.shape
    #numpy matrix with size?
    new_img=np.zeros(shape=(rows,cols))
    #nested loop to copy values from input to output using equation out_value=255-invalue (this is inverse)
    for i in range(rows):
        for j in range(cols):
            new_img[i][j]=255-inImage[i][j]

    maxPixel=0
    #find max pixel value of origional image
    for row in range(rows):
        for col in range(cols):
         # get the current pixel value
            currentPixel = inImage[row, col]
            # Manipulating your pixel values
            if currentPixel > maxPixel:
                maxPixel=currentPixel
    print("The max pixel is ",maxPixel) 
    
    maxPixel=0
    currentPixel=0
    #find max pixel of updated image
    for row in range(rows):
        for col in range(cols):
         # get the current pixel value
            currentPixel = new_img[row, col]
            # Manipulating your pixel values
            if currentPixel > maxPixel:
                maxPixel=currentPixel
    print("The max pixel is ",maxPixel) 
    return new_img

  




