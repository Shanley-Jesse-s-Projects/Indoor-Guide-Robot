#import L3_drivingPatterns as drive
import morethansad as more
import summaryMatrix as sum_ma
import allMight as al_mi
import L2_log as log
import L2_vector as vector
import numpy as np
from math import *
import time
import L2_speed_control as sc
import L1_motors as m
import L1_motors as mot
import csv


#the purpose of this code is to combine the previous codes to move the robot
#and save the data.

#Get the inital data needed

#The purpose of this function is to stop the robot from moving.
def stop():
    m.MotorL(0)
    m.MotorR(0)
def go_front():
    m.MotorL(10)
    m.MotorR(10)


#The robot can make a circle to turn around.
def turn_around():
    duties = sc.openLoop(10, -10) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors
    

def boundingCircle(why):   #bounding circle method obstacle avoidance
    boundingRadius=.4
    go_front()
    for i in why:
        n = np.array(why)
    c=n[0]
    print(c)
    if c < boundingRadius:
        turn_around()
        print("turning around")
        
    return


       
    # if c < .18:   #only looks at greater than 7 inches and filters for bad values. 
    #     if c < boundingRadius:
    #         c=0
    #         c=n[0]
    #         print(c)
    #         if c < boundingRadius:
    #             c=n[0]
    #             print(c)
    #             stop()
    #         #c=0
               
                    
    
    print("no object within radius")
    #go_front()
    return

while(1):
    why = vector.getNearest()
    boundingCircle(why)
    time.sleep(.386)
