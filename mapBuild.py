#the function of this program is to build a map of xy coordinates based on the output from the lidar. 
#The points are mapped relative to the current position of the robot. 
#code written by Jesse Rosart-Brodnitz in January 2020
#contact: jorbaustin@gmail.com

#over extended distances, the error can compound

#all the lidar data gets processed at once, which means the the processing will not occur until each scan has been completed



import L1_lidar as lidar   #the imported file was provided through the MXET 300 class. 
import math
import numpy as np
import time
import summaryMatrix as sumsum
import csv
import L2_log		#the imported file was provided through the MXET 300 class. 
import L2_vector as vec #the imported file was provided through the MXET 300 class with adapatations. 
from subprocess import call
import L2_heading as header	#the imported file was provided through the MXET 300 class with adaptations. 

def globeLidar (d, theta, xprime, yprime, øprime):      #takes in Lidar data and initial coordinates and outputs global coordinates of lidar data. 
    # print("the value of d is: ", d)
    # print("the value of ø is: ", theta*180/np.pi)
    theta=localize(theta)       #localize each element with respect to the x axis of global. takes in lidar column1, angles
    xp2=d*np.sin(theta) #finds local x, also p0p1 term goes to 0 because lidar is approx origin
    yp2=d*np.cos(theta) #finds local y
    xp2Prime=np.cos(øprime)*xp2-np.sin(øprime)*yp2+xprime #finds global x of lidar scan instance
    yp2Prime=np.sin(øprime)*xp2+np.cos(øprime)*yp2+yprime #finds global y of lidar scan instance
    xp2Prime = np.reshape(xp2Prime,(xp2Prime.shape[0], 1))      #turns row into column
    yp2Prime = np.reshape(yp2Prime,(yp2Prime.shape[0], 1))      #turns row into column
    globeXY = np.array([xp2Prime, yp2Prime])        #combines both columns into array
    return(np.round(globeXY, 3))
    
    
def localize(theta):    #localize each element with respect to the x axis of global
    #scan through every element of an array, find the quadrant of each and do the necessary math to localize with respect to the global y axis
    #before hand, theta will be measuring deviations from the robot x axis, 

    theta=theta*180/np.pi
    for x in np.nditer(theta, op_flags=['readwrite']):      
        if x[...] < 0:        #checks quadrant 2 and 3
            x[...]=abs(x)+90
        else:                   #checks quadrant 1 and 4
            x[...]=90-x
            if x[...] < 0:
                x[...]=x+360
    #print(theta) 
    theta=theta*np.pi/180
    return(theta)
    
    
def callMapBuild(xprime, yprime, numDataPoints, clearFile):

    lidarData=lidar.polarScan(numDataPoints)       #lidar scan, should output a 2 column array
    lidarData=vec.getValid(lidarData)   #checks for valid data, removes invalid and values less than 16 mm from lidar data
    d=lidarData[:,0]                      #takes first column of lidar array
    ø=lidarData[:,1]                       #takes second column of lidar array  #degrees
    øprime=looking()             

    sumMatrix=sumsum.task1(xprime, yprime, øprime)      #gets x, y, ø from summary matrix   øprime is accepted in degrees
    xprime=sumMatrix[0]                                 #x value for reinsertion into summary matrix
    yprime=sumMatrix[1]                                 #y value for reinsertion into summary matrix
    øprime=sumMatrix[3]*np.pi/180                       #ø value for reinsertion into summary matrix        
       

    ø=ø*np.pi/180   #converts to radians
    print(øprime*180/np.pi) 						 #prints theta prime in degrees for debug
    g=globeLidar(d, ø, xprime, yprime, øprime)

    if clearFile ==1:
        clear_fileX()
        clear_fileY()
    return(g)
    
 #usage example
    #example of how you call it:
        # xprime=0        
        # yprime=0
        # øprime=0  
        # numDataPoints = 360
        # x=callMapBuild(xprime, yprime, øprime, numDataPoints)
        # print(x)
	   # an_array = np.array([1, 1, 1, 1, 1, 1, 10])
	   # mean = np.mean(an_array)
	   # standard_deviation = np.std(an_array)
        # distance_from_mean = abs(an_array - mean)
        # max_deviations = 2
        # not_outlier = distance_from_mean < max_deviations * standard_deviation
        # no_outliers = an_array[not_outlier]


#file write functions block/////////////////
def clear_fileX():
    open('mapxg.csv','w').close()       #change file names for new file
def clear_fileY():
    open('mapyg.csv','w').close()       #change file names for new file
    
def csv_writeX(list):
    list = [str(i) for i in list]
    with open('mapxg.csv', 'a') as csvFile:     #change file names for new file
        writer = csv.writer(csvFile)
        writer.writerow(list)
    csvFile.close()
def csv_writeY(list):
    list = [str(i) for i in list]
    with open('mapyg.csv', 'a') as csvFile:         #change file names for new file
        writer = csv.writer(csvFile)
        writer.writerow(list)
    csvFile.close()
    
    

def pathPlot(xprime, yprime):     #the goal of this will be to take in 
#(in iterations) the x and y points and output the to a file
#pass in init x and init y 

    csv_writeXpath(xprime)
    csv_writeYpath(yprime)
    return("done")
 
def looking():  #calls the heading function (uses the magnetometer)
    axes = header.getXY() # call xy function
    axesScaled = header.scale(axes) # perform scale function
    h = header.getHeading(axesScaled) # compute the heading
    #headingDegrees = round(h,2)     #should come in as radians
    return(h)

	
if __name__ == “__main__”
	 xprime= 0       
	 yprime=0
	 #print(øprime)
	 numDataPoints =400 #27 should take a reading every 10 degrees
	 clearFile=0 #1 for clear, 0 for keep adding points to file
	 for x in range (0,1):
	     y=callMapBuild(xprime, yprime, numDataPoints, clearFile)
	     print(y)
	     #print(x)
