#moveMap 
#this programs builds a map of XY points based on odometry and processed lidar readings. The program outputs two csv files containing a list of x points and a list of y points. 
#these points can then be graphed to visualize the map through excel or a similar CSV reading program. 
#code written by Jesse Rosart-Brodnitz in January 2020
#contact: jorbaustin@gmail.com

import mapBuild as mapmap
import summaryMatrix as sumsum
import math
import numpy as np
import time
import L2_speed_control as sc   #the imported file was provided through the MXET 300 class. 
import L1_motors as m           #the imported file was provided through the MXET 300 class with adaptations. 
import L2_heading as header     #the imported file was provided through the MXET 300 class. 
import loopDrive as chino

#////////////Motion block//////////////////

def stop(): #The purpose of this function is to stop the robot from moving.

    m.MotorL(0)
    m.MotorR(0)

def go_front():#The purpose of this function is to have the robot move foward.

    duties = sc.openLoop(7.7, 7.7) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors
           

def go_back():#The purpose of this function is to have the robot move backwards.

    duties = sc.openLoop(-7.7, -7.7) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors

def turn_around():#The robot turns around (pdl and pdr configured for 2 second turn of pi.

    duties = sc.openLoop(7.7, -7.7) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors



#//////////////////////////
def callmaptrack(xprime, yprime, numDataPoints, clearFile, pdl, pdr, runTime):#THIS IS A DEBUG FUNCTION ONLY.  USES MOTORS      #uses open loop control
    wx=[]   #inits x array
    wy=[]   #inits y array
    if clearFile ==1:       #empties map csv
        mapmap.clear_fileX()    #clears X
        mapmap.clear_fileY()    #clears Y
    np.set_printoptions(suppress=True)
    
    duties = sc.openLoop(pdl, pdr) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors
    
    for p in range(0,runTime):        #how long I want it to run
        øprime=np.pi/2
        q=mapmap.callMapBuild(xprime, yprime, numDataPoints, 0) #converts lidar data to global
      
        sumMatrix=sumsum.task1(xprime, yprime, øprime)      #gets x, y, ø from summary matrix
        xprime=sumMatrix[0]                                 #x value for reinsertion into summary matrix
        yprime=sumMatrix[1]                                 #y value for reinsertion into summary matrix
     
                                 #ø value for reinsertion into summary matrix
        wx.extend(q[0])             #adds x data points onto end of array
        wy.extend(q[1])              #adds Y data points onto end of array

    mapmap.csv_writeX(wx)
    mapmap.csv_writeY(wy)
    globeXY = np.array([wx, wy])
    print("finished ")
    return(globeXY)
    
    
    
def callmapping(xprime, yprime, numDataPoints, clearFile, runTime):
    wx=[]   #inits x array
    wy=[]   #inits y array
    if clearFile ==1:       #empties map csv
        mapmap.clear_fileX()    #clears X
        mapmap.clear_fileY()    #clears Y
    np.set_printoptions(suppress=True)
    
  
    for p in range(0,runTime):        #how long I want it to run
        øprime=np.pi/2
        q=mapmap.callMapBuild(xprime, yprime, numDataPoints, 0) #converts lidar data to global
        
        sumMatrix=sumsum.task1(xprime, yprime, øprime)      #gets x, y, ø from summary matrix
        xprime=sumMatrix[0]                                 #x value for reinsertion into summary matrix
        yprime=sumMatrix[1]                                 #y value for reinsertion into summary matrix
                                         #ø value for reinsertion into summary matrix
        wx.extend(q[0])             #adds x data points onto end of array
        wy.extend(q[1])              #adds Y data points onto end of array

    mapmap.csv_writeX(wx)
    mapmap.csv_writeY(wy)
    globeXY = np.array([wx, wy])
    print("finished ")
    return(globeXY)


def callClosedmaptrack(xprime, yprime, numDataPoints, clearFile, runTime):#THIS IS A DEBUG FUNCTION ONLY.  USES MOTORS      #uses closed loop control
    wx=[]   #inits x array
    wy=[]   #inits y array
    if clearFile ==1:       #empties map csv
        mapmap.clear_fileX()    #clears X
        mapmap.clear_fileY()    #clears Y
    np.set_printoptions(suppress=True)
    
    chino.drivingMeInsane()
    
    
    for p in range(0,runTime):        #how long I want it to run
        øprime=np.pi/2
        q=mapmap.callMapBuild(xprime, yprime, numDataPoints, 0) #converts lidar data to global
      
        sumMatrix=sumsum.task1(xprime, yprime, øprime)      #gets x, y, ø from summary matrix
        xprime=sumMatrix[0]                                 #x value for reinsertion into summary matrix
        yprime=sumMatrix[1]                                 #y value for reinsertion into summary matrix
        print(xprime, yprime)
                                 #ø value for reinsertion into summary matrix
        wx.extend(q[0])             #adds x data points onto end of array
        wy.extend(q[1])              #adds Y data points onto end of array
    sc.stopDrive                    #braking start method  
    sc.driveClosedLoop(0, 0, 0)     #breaking method to bring the PID controller values back to 0
    m.MotorL(0)                     #motor overrides
    m.MotorR(0)
    mapmap.csv_writeX(wx)           #writes points to file
    mapmap.csv_writeY(wy)           
    globeXY = np.array([wx, wy])    #combines two columns into array for return
    print("finished ")              #finished statement for debug   
    return(globeXY)                 #sends out array of points for x and y


def threadRun():    #callable function to run moveMap with threading
    callmapping(0, 0, 22, 1, 14)        #sets x and y to start at 0, 22 data points per scan, clear file, repeat 14 times. 
    
if __name__ == "__main__":
    callmapping(0, 0, 600, 1, 1)      #sets x and y to start at 0, 600 data points per scan, clear file, repeat 1 time.

