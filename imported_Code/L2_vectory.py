#NOT OUR CODE. BASE File PROVIDED THROUGH THE MXET 300 CLASS, MODIFIED
# This program manipulates distance vectors in the robot coordinate frame,
# as well as arrays of vectors.  Pay attention to format of arguments since
# some functions are not yet optimized to handle numpy [1x2] vectors directly.
# Further functions will be added for rotation of vectors in various coordinate frames.

# Import external libraries
import numpy as np
from numpy import exp, abs, angle
import time

# Import internal programs
import L1_lidar as lidar

np.set_printoptions(precision=3) # after math operations, don't print long values



def outlierRemoval(array, deviations):
    mean=np.mean(array)
    standard_deviation = np.std(array)
    distance_from_mean = abs(array - mean)
    not_outlier = distance_from_mean < deviations * standard_deviation
    no_outliers = array[not_outlier]
    return(no_outliers)



def getValid(scan): # remove the rows which have invalid distances
    dist = scan[:,0] # store just first column
    angles = scan[:,1] # store just 2nd column
    outlierRemoval(dist, 1)
    valid = np.where(dist > .05) # find values 16mm This was alterted to be 12 inches instead
    myNums = dist[valid] # get valid distances
    myAng = angles[valid] # get corresponding valid angles
    output = np.vstack((myNums,myAng)) # recombine columns 
    n = output.T # transpose the matrix
    return n

def nearest(scan): # find the nearest point in the scan
    dist = scan[:,0] # store just first column
    column_mins = np.argmin(dist, axis=0) # get index of min values along 0th axis (columns)
    row_index = column_mins#[0] # index of the smallest distance
    vec = scan[row_index,:] # return the distance and angle of the nearest object in scan
    return vec # contains [r, alpha]

def polar2cart(r,alpha):  #convert an individual vector to cartesian coordinates (in the robot frame)
    alpha = np.radians(alpha) #alpha*(np.pi/180)  # convert to radians
    x = r * np.cos(alpha) # get x
    y = r * np.sin(alpha) # get y
    cart = np.round(np.array([x, y]),3) #vectorize and round
    return cart

def rotate(vec,theta): # describe a vector in global coordinates by rotating from body-fixed frame
    c, s = np.cos(theta), np.sin(theta) # define cosines & sines
    R = np.array(((c,-s), (s, c))) #generate a rotation matrix
    vecGlobal = np.matmul(R,vec) # multiply the two matrices
    return vecGlobal 

def sumVec(vec,loc): # add two vectors. (origin to robot, robot to obstacle)
    mySum = vec + loc # element-wise addition takes place
    return mySum # return [x,y]

def getNearest(): # combine multiple functions into one.  Call to get nearest obstacle.
    scan = lidar.polarScan() # get a reading in meters and degrees
    valids = getValid(scan) # remove the bad readings
    vec = nearest(valids) # find the nearest
    return vec # pass the closest valid vector [m, deg]

# UNCOMMENT THE LOOP BELOW TO RUN AS A STANDALONE PROGRAM
# while 1:
#     myVector = getNearest() # call the function which utilizes several functions in this program
#     print("\n The nearest object (m,deg):\n", myVector) # print the result
#     time.sleep(0.1) # small delay
# myVector = getNearest() # call the function which utilizes several functions in this program
# print("\n The nearest object (m,deg):\n", myVector) # print the result
# time.sleep(0.1) # small delay
