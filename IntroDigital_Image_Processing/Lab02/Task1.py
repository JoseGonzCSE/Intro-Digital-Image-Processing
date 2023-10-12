
from hashlib import new
from PIL import Image,ImageOps

import numpy as np
from numpy import asarray

#read iamge
im=Image.open('Beginnings.jpg')
#show
im.show()
#greyscale
im_gray=ImageOps.grayscale(im)
#show
im_gray.show()
#pixel values from image into im_gray_pixels.
im_gray_pixels=asarray(im_gray)

#get the values for rows and columns and prints out the values
rows,cols=im_gray_pixels.shape
print("Image size is: ",rows,"rows x",cols,"columns")

#nested for loops to compute max pixel and print it out 
maxPixel=0
#find max pixel
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        currentPixel = im_gray_pixels[row, col]
        # updates maxpixel with the largest value
        if currentPixel > maxPixel:
            maxPixel=currentPixel
print("The max pixel is ",maxPixel)



#creating a new matrix 
newRow=cols
newCol=rows
im_gray_90_pixels = np.zeros(shape=(newRow,newCol))

#counterclockwise of image
#533 pixel value
reverse=cols-1
for i in range(len(im_gray_90_pixels)):
    for j in range (len(im_gray_90_pixels[0])):
        im_gray_90_pixels[i][j]=im_gray_pixels[j][reverse]
    reverse=reverse-1

# save the counterclockwise of image and show 
imRotatecounter = Image.fromarray(np.uint8(im_gray_90_pixels))
imRotatecounter.show()
imRotatecounter.save("Beginnings_grayscale_counterClock.jpg")

#clockwise
im_gray_90_pixels = np.zeros(shape=(newRow,newCol))
reverse=rows-1

for i in range(len(im_gray_90_pixels[0])):
    for j in range (len(im_gray_90_pixels)):
        im_gray_90_pixels[j][i]=im_gray_pixels[reverse][j]
    reverse=reverse-1
#save the clockwise of image and show
imRotateclock = Image.fromarray(np.uint8(im_gray_90_pixels))
imRotateclock.show()
imRotateclock.save("Beginnings_grayscale_clock.jpg")

#nested for loops to compute max pixel and print it out for the clockwise
maxPixel=0
currentPixel=0
#find max pixel
for i in range(newRow):
    for j in range(newCol):
        # get the current pixel value
        currentPixel = im_gray_90_pixels[i, j]
        # Manipulating your pixel values
        if currentPixel > maxPixel:
            maxPixel=currentPixel

print("The max pixel is for the clockwise is ",maxPixel)




