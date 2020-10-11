import numpy as np # for array handling
import pysicktim as lidar # required for communication with 781 lidar sensor
import time # for timekeeping
import math
import L2_log as log
import csv


np.set_printoptions(suppress=True)
start_angle = -135.0 # lidar points will range from -135 to 135 degrees. this outputs a range of 270. 

def testScan(num_points=270):
    lidar.scan()    #starts reading
    
    
    
    dist_amnt = lidar.scan.dist_data_amnt   # Number of distance data points reported from the lidar
    angle_res = lidar.scan.dist_angle_res   # Angular resolution reported from lidar
    
    scan_points = np.asarray(lidar.scan.distances)  #turns into an array
    inc_ang = (dist_amnt/(num_points+1))*angle_res  # Calculate angle increment for scan_points resized to num_points
    scan_points = np.asarray(np.array_split(scan_points,num_points))  # Split array into sections
    scan_points = [item[0] for item in scan_points]   # output first element in each section into a list
    scan_points = np.asarray(scan_points) # cast the list into an array
    scan_points = np.reshape(scan_points,(scan_points.shape[0],1)) # Turn scan_points row into column

    angles = np.zeros(num_points)   #initilizes the angles array by setting it to the size of data points and filling it with zeros 
    
    x = len(angles)
    for i in range(x): #run this loop
        angles[i] = (i*lidar.scan.dist_angle_res*lidar.scan.dist_data_amnt/num_points)+(start_angle)
        xlocal = scan_points*math.cos(angles[i])    #convertz lidar data into local x for lidar
        ylocal = scan_points*-math.sin(angles[i])    #convertz lidar data into local y for lidar
        #print(angles[i])
     #   xglobal=math.cos(angles[i])*xlocal-math.sin(angles[i])*ylocal
      #  yglobal=math.sin(angles[i])*xlocal+math.cos(angles[i])*ylocal
       # xgloballog=xglobal
        

    #break into local x and local y
    local = np.asarray(xlocal)  #turns into an array
    
    #print("the local X is ", xlocal)    #prints the local x
    #print("the local Y is ", ylocal)    #prints the local y
   
    local = np.hstack((xlocal,ylocal))    #combines the lists into one array. 
    #print(local)    #prints the array. 
    
    #local to global
  #  earth=np.asarray(xglobal)               #turns into an array        
   # earth= np.hstack((xglobal, yglobal))    #turns xglobal and y global into 1 array
    print("global:", earth)    #prints global
    xg=xgloballog
    xgc = xg[0]
    log.uniqueFile(local, "localEarthHistory.csv")
    
    
    #     PdC = kin.getPdCurrent() #in rad/s, wheel speeds, phidots
    # xPdCurrent = PdC[0]     #x is left
    # yPdCurrent = PdC[1]     #y is right
    # print("printing pdl and pdr in rads/sec", PdC)
    # log.uniqueFile(PdC[0], "pdl.txt")
    # log.uniqueFile(PdC[1], "pdr.txt")
    
    
testScan(270)    #runs the program x times
