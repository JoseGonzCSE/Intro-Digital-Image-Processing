# MyImageFunctions.py
# Import pillow
from PIL import Image, ImageOps  # Import numpy
import numpy as np
from numpy import asarray
# For sqrt(), floor()
import math


def myImageResize(inImage_pixels, M, N, interpolation_method):
    # HEADER:
    # Input: a numpy matrix of the image that will be downscaled or upscaled, the number of rows in the resized image,
    # the number of columns in the resized image, a string that will determined the method of interpolation ("nearest" or
    # "bilinear")
    # This function will resize the original image by using nearest neighbor or bilinear interpolation
    # Output: a new numpy matrix of the image that was resized

    new_array = np.zeros([M, N], dtype=np.float32)
    rows, columns = inImage_pixels.shape

    # creating new locations from the original image
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            # These eqs. help find a location for each pixel of the resize image to a location to the original image.
            # want to determine the location of x and y in the original image, so we can see which pixels values are the closest
            # to x and y in the original image
            x = ((rows/M) * (m - 0.5)) + 0.5
            y = ((columns/N) * (n - 0.5)) + 0.5

            # the interpolation method is nearst neighbor
            if interpolation_method == "nearest":
                # round the number of the locations calculated by the formula
                x_pix_loc = round(x)
                y_pix_loc = round(y)
                # insert those values into the new image matrix
                new_array[m-1, n-1] = inImage_pixels[x_pix_loc-1, y_pix_loc-1]

            # the interpolation method is bilinear
            else:
                # First determine the two closest pixels to x
                x1 = 0
                x2 = 0
                y1 = 0
                y2 = 0
                if x == int(x):
                    x1, x2 = x
                elif x < 1:
                    x1 = 1
                    x2 = 2
                elif x > rows - 1:  # use the bound of the orignal image
                    x1 = rows - 2
                    x2 = rows - 1
                else:
                    x1 = math.floor(x)
                    x2 = math.ceil(x)

                # Then find the two closest pixels to y
                if y == int(y):
                    y1, y2 = y
                elif y < 1:
                    y1 = 1
                    y2 = 2
                elif y > columns - 1:  # use the bound of the original image
                    y1 = columns - 2
                    y2 = columns - 1
                else:
                    y1 = math.floor(y)
                    y2 = math.ceil(y)

                # Then find the four pixel values using the closest pixels values of x and y
                # 4 pixel values need = (x1,y1), (x1,y2), (x2, y1), (x2, y2)

                first_pixel = inImage_pixels[int(x1)-1, int(y1)-1]
                sec_pixel = inImage_pixels[int(x1)-1, int(y2)-1]
                thr_pixel = inImage_pixels[int(x2)-1, int(y1)-1]
                four_pixel = inImage_pixels[int(x2)-1, int(y2)-1]

                # Send the 4 pixel location, and the 4 pixel location values, the original x and y locations (which were calculated up above using slope intercept formula)
                new_array[m-1, n-1] = mybilinear(x1, y1, first_pixel, x1,
                                                 y2, sec_pixel, x2, y1, thr_pixel, x2, y2, four_pixel, x, y)
    return new_array


def myRMSE(first_im_pixels, second_im_pixels):
    # HEADER:
    # Input: two numpy matrices of the same dimension
    # Calculates the difference between two matrices between the original image and the reconstructed image
    # Output: Returns the RMSE value

    rows, columns = first_im_pixels.shape
    # rows and columns is the dimension of the matrix
    total = 0

    for r in range(rows - 1):
        for c in range(columns - 1):
            # Find the difference of the pixel value between the same pixel location from both matrices
            cost = first_im_pixels[r, c] - second_im_pixels[r, c]
            total = (cost * cost) + total
    total = (1/(rows * columns))*total
    RMSE = math.sqrt(total)

    return RMSE


def mybilinear(x1, y1, p1, x2, y2, p2, x3, y3, p3, x4, y4, p4, x5, y5):
    # HEADER:
    # INPUT: The input is the locations in the x and y directions which create 4 different coordinates from the orignal image,
    # need the pixel value from the 4 different coordinates, and
    # the orignal location calculated up above from the resized image to the orignal image.
    # FUNCTION: Calculate the new pixel value from the 4 different coordinates using linear interpolation
    # OUTPUT: A new pixel value calculated by bilinear interpolation

    # linear interpolations in the x-direction
    fir_value = (p3 - p1)*((x5 - x1) / (x3 - x1)) + p1
    # linear interpolations in the x-direction
    sec_value = (p4 - p2)*((x5 - x2) / (x4 - x2)) + p2
    interValue = (sec_value - fir_value)*((y5 - y3) / (y4 - y3)) + fir_value
    # linear interpolations in the y-direction

    return interValue
