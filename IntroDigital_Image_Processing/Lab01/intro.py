import numpy as np
from numpy import asarray

# Create two-dimensional data structures (images) and setting their values to zero
a = np.zeros(shape=(6, 6))
a[0,0] = 2       # assign value by index
a[1:3, 0:4] = [[0,1,2,3], [2,3,4,5]]  # assign value by slicing

# loop a matrix with 2 for loops
row, col = a.shape
for r in range(row):
    for c in range(col):
        if a[r,c] != 0:   # using if statement to check the value
            print('current value is: ', a[r,c])


####################################################################
# Matrix arithmetic
####################################################################

# 1. dot product: It is the sum of the products of the corresponding elements in the two matrices.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6, 7], [8, 9, 10]])
print("dot:", np.dot(a, b))

# 2. trasnpose: switching its rows with its columns.
a = np.array([[1, 2], [3, 4], [5, 6]])
print("\nWith np.transpose(a) function")
print(np.transpose(a))

print("\nWith ndarray.transpose() method")
print(a.transpose())

# 3. Mean: Returns the average of the matrix elements along the given axis.
a.mean()

# 4. Return the maximum value along an axis.
a.max()

# 5. Return the minimum value along an axis.
a.min()


####################################################################
# Basic image operation
####################################################################
# import pillow
from PIL import Image, ImageOps

# open a image from path
im = Image.open('puppy.jpg')

# show the image
im.show()

# resize the image
new_size = (256, 256)
im_resize = im.resize(new_size)

# save the image to target path
im_resize.save('my_puppy.jpg')

# print image size
print("previous image size is: ", im.size)
print("modified image size is: ", im_resize.size)

# read image to numpy array
data = asarray(im_resize)

# print shape of your numpy array
print(data.shape)

# convert image to gray scale
im_gray = ImageOps.grayscale(im_resize)
im_gray_path = 'my_gray_puppy.jpg'
im_gray.save(im_gray_path)

# loop all the pixels of the image
im_gray_pixels = asarray(Image.open(im_gray_path))
print("current shape is: ", im_gray_pixels.shape)

rows, cols = im_gray_pixels.shape

# get all the pixel values using the index
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_pixels[row, col]
        # Manipulating your pixel values
        # for example: print pixel values that are greater than 200
        if current_pixel_value > 250:
            print("current pixel value is greater than 200: ", current_pixel_value)



################################################
# Function
################################################
def myFirstFunction(a,b):
    print(a+b)

myFirstFunction(46,64)
myFirstFunction('46','64')

################################################
# Call Function from Another File
################################################

import myfunc
from myfunc import subtractNumbers,divideNumbers

# call function
myfunc.addNumbers(456,654)
subtractNumbers(654,321)
divideNumbers(462,7984)

#cannot call multiplyNumbers directly at this time since it's not imported
#multiplyNumbers(546,7)
myfunc.multiplyNumbers(546,7)


################################################
# Plotting Images using Matplotlib
################################################
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
import numpy as np

# display image using plt.imshow
im = Image.open('puppy.jpg')
plt.imshow(im)
plt.show()

# plot lines
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints,ypoints)
plt.show()

# plot scatters
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()


# plot bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

# plot histogram
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
