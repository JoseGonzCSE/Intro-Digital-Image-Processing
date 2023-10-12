# MyHEFunctions.py

# Import numpy
import numpy as np
from numpy import asarray

def compute_histogram( image_pixels ):

    # Function that will compute the histogram for the inputed pixels
    # uses the rows/colums and some really cool math to compute the histogram

    # m= rows, n=colums
    Minput, Ninput = image_pixels.shape
    #create vector
    hist = np.zeros(shape=(256)) 

    #for loop to begin the histogram process
    for i in range(Minput):
        for j in range(Ninput):
            matrix= image_pixels[i,j]
            matrix+=1
            hist[int (image_pixels[i][j])] +=1

    #sum initializer
    sum= 0
    #final part of the histogram calculation
    for matrix in range(256):
        sum=sum+hist[matrix]

    hist/=sum
    #returns the histogram
    return hist

   
def equalize( in_image_pixels ):
   #Equalize function to equalize an inputed image
   # Uses the math for Equalization and the normalized histogram function above to determine the transformation

    #rows/colums
    Minput, Ninput = in_image_pixels.shape

    #normalized historgram
    NormalizedHistogram=compute_histogram(in_image_pixels)
    # 256 length numpy vector 
    Transformation = np.zeros(shape=(256)) 

    #computes entries in transfomation vector using norbalized histogram                          
    for i in range(256):
        for k in range(i):
            Transformation[i]+=NormalizedHistogram[k]
        Transformation[i]=255*Transformation[i]



  
    
    #numpymatrix for output
    out_image_pixels = asarray(in_image_pixels, dtype=np.float32)
    #Transformation vector to transform each pixel in input image into the output
    for i in range (Minput):
        for j in range(Ninput):
            out_image_pixels[i,j]=Transformation[int(in_image_pixels[i][j])]
    return out_image_pixels

    




def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
