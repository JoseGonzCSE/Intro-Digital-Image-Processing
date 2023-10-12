from PIL import Image,ImageOps
from grpc import xds_server_credentials

import numpy as np
from numpy import asarray
#sqrt and floor function
import math   

def myImageResize( inImage_pixels, M, N, interpolation_method ):
    #Function to resize an image using the pixels, rows,colums, and interpolation method of either bilinear or nearest neighbor

    #gets the rows/colums
    Minput, Ninput = inImage_pixels.shape
    # create a new output matrix
    out = np.zeros(shape=(M, N))

    #Beggining of interpolation 
    for m in range(M+1):  # int
        for n in range(N+1):   # int
            # loop  all the pixels from the out

            # 1. we estimate the index of input image -> estimate row and col
            m_inter = (((m-0.5)/M) * Minput) + 0.5   # folat number,
            n_inter = (((n-0.5)/N) * Ninput) + 0.5

            # 1.2， 2.7
            # 300.5， 396.8

            #Nearest neighbor interpolation    
            if interpolation_method == 'nearest':
                # use nn
                # round()
                m_inter = round(m_inter)
                n_inter = round(n_inter)
                #print("m_inter: ", m_inter)
                #print("n_inter: ", n_inter)  # 100 x 175
                out[m-1, n-1] = inImage_pixels[m_inter-1,n_inter-1]
            #Bilinear interpolation
            elif interpolation_method == 'bilinear':
                # use the bilinear

                # 1.2， 2.7
                # 300.5， 396.8

                # find the 4 points
                # use the if else from the hw
                # m_inter -> m1, m2  which are the nearest row index
                if m_inter == int(m_inter):
                    m1= m_inter-1
                    m2= m_inter-1
                elif m_inter < 1:
                        m1= 1
                        m2= 2
                elif m_inter > Minput-1:
                        m1= Minput - 2
                        m2= Minput -1
                else:
                        m1= math.floor(m_inter-1 )
                        m2= math.ceil(m_inter-1 )
                        
                # n_inter -> n1, n2  which are the nearest col index
                if n_inter == int(n_inter):
                    n1= n_inter -1
                    n2= n_inter -1
                elif n_inter < 1:
                        n1= 1
                        n2= 2
                elif n_inter > Ninput-1 :
                        n1= Ninput - 2
                        n2= Ninput -1
                else:
                        n1= math.floor(n_inter-1 )
                        n2= math.ceil(n_inter-1)
                

                



                #m -> x
                #n -> y
                #p -> inImage_pixels[m_, n_]
                #after you have m1, m2, n1, n2 -> 4 points
                #p1, m1, n1
                #p2, m1, n2
                #p3, m2, n1
                #p4, m2, n2
                #m_inter, n_inter ----> p5

                #print("x1, y1, p1: ", m1, n1, p1)
                #print("x2, y2, p2: ", m1, n1, p1)
                ...
               # print("x5, y5: ", m1, n1, p1)   1.2, 11.8  -> 1, 2  11,12

                #p5 = mybilinear(m1,n1,p1,m2,n2,p2 ... )

                #finding our 5 values for interpolation 
                p1 = inImage_pixels[m1, n1]
                p2 = inImage_pixels[m1, n2]
                p3 = inImage_pixels[m2, n1]
                p4 = inImage_pixels[m2, n2]

                #getting our 5th value using my bilinear function then outputing it onto a new matrix
                p5 = mybilinear(m1,n1,p1,m1,n2,p2,m2,n1,p3,m2,n2,p4,m_inter-1,n_inter-1)
                out[m-1, n-1] = p5

    return out


#Root mean square deviation for pixel values, helps us in multiple location and helps us determine the quality of an image 
def myRMSE( first_im_pixels, second_im_pixels ):
    # I1, I2
    I1=first_im_pixels
    I2=second_im_pixels

    #Math for root mean square deviation for pixel values
    total = 0
    M,N = np.shape(I1)
    for m in range(M):
        for n in range(N):
            total += pow(I1[m,n]-I2[m,n],2)

    # now you have sum
    total = total / (M * N)

    return math.sqrt(total)

#Bilinear function gathered from hw 01 and implemented here
def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5):
    # use eq from hw
    # apply eq on p1 and p3  -> t1
    # apply eq on p2 and p4  -> t2
    # ....        t1 and t2  -> p5

    ...
    t1 = (p3 - p1)*((x5 - x1)/(x3 - x1)) + p1
    t2 = (p4-p2)*((x5-x2)/(x4-x2)) + p2
    p5 = (t2 - t1)*((y5-y1)/(y2-y1)) + t1
    ...
    return p5 
