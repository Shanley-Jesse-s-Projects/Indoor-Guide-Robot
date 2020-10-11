#Code co-writen by: Shanley Mullen, Jesse Rosart-Brodnitz
#email: shanleymullen@gmail.com, jorbaustin@gmail.com
import boundingSqure as mp1
import L2_vector as vector #the imported file was provided through the MXET 300 class with adaptations
import numpy as np
from math import *
import time
import L2_speed_control as sc  #the imported file was provided through the MXET 300 class. 
import L1_motors as m  #the imported file was provided through the MXET 300 class. 
import csv
import speechInOut as speech
# the purpose of this code is to combine the previous codes to move the robot
# and save the data as a map in excel. This code also uses obstacle avoidance.

# Get the inital data needed
global P_0
P_0 = [.1651, .0254]
Globes = []


# The purpose of this function is to stop the robot from moving.
def stop():
    m.MotorL(0)
    m.MotorR(0)

# The purpose of this function is to have the robot move forward.
def go_front():
    duties = sc.openLoop(7.7, 7.7)  # produce duty cycles from the phi dots
    m.MotorL(duties[0])  # send command to motors
    m.MotorR(duties[1])  # send command to motors

# The purpose of this function is to have the robot move backwards.
def go_back():
    duties = sc.openLoop(-7.7, -7.7)  # produce duty cycles from the phi dots
    m.MotorL(duties[0])  # send command to motors
    m.MotorR(duties[1])  # send command to motors

# The robot can make a circle to turn around.
def turn_around():
    duties = sc.openLoop(1.28, -1.28)  # produce duty cycles from the phi dots
    m.MotorL(duties[0])  # send command to motors
    m.MotorR(duties[1])  # send command to motors

def boundingCircle(why):  # bounding circle method obstacle avoidance
    boundingRadius = .3556
    for i in why:
        n = np.array(why)
    c = n[0]
    print(c)
    if c < .254:  # only looks at greater than 7 inches and filters for bad values.
        if c < boundingRadius:
            c = 0
            c = n[0]
            print(c)
            if c < boundingRadius:
                c = n[0]
                print(c)
                stop()
                # c=0
                ans = speech.twelvetwee()
                if ans == "yes":
                    go_back()
                    turn_around()
                    return
                if ans == "no":
                    go_front()
                    return

    print("no object within radius")
    go_front()
    return

# Put everything together to save to a map function.
def im_the_map(x_g, y_g):
    xyGlobal = np.array([x_g, y_g])
    mapCoordinates = xyGlobal
    return (mapCoordinates)

def clear_file():
    open('map.csv', 'w').close()


def csv_write(list):
    list = [str(i) for i in list]
    with open('map.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(list)
    csvFile.close()

clear_file()
while (1):
    #Get all the different varaibles needed to find the points
    point = vector.getNearest()
    x_int = mp1.x(point)
    y_int = mp1.y(point)
    x_l = mp1.lidar_mathx(x_int, mp1.P_1x(x_int, y_int, point), P_0, point)
    y_l = mp1.lidar_mathy(y_int, mp1.P_1y(x_int, y_int, point), P_0, point)
    one = mp1.P_1x(x_int, y_int, point)
    two = mp1.P_1y(x_int, y_int, point)
    x_g = mp1.x_global(point, x_int, two, one, x_l, y_l)
    y_g = mp1.y_global(point, y_int, two, one, x_l, y_l)

    w = im_the_map(x_g, y_g)
    csv_write([w])

    one = mp1.P_1x(x_int, y_int, point)
    two = mp1.P_1y(x_int, y_int, point)
    x_g = mp1.x_global(x_int, y_int, two, one, x_l, y_l)
    y_g = mp1.y_global(x_int, y_int, two, one, x_l, y_l)
    im_the_map(x_g, y_g)
    if why[0] < .4318:  # 17 inches - the largest length of the robot
        if why[0] < .3556:  # Change less than to greater than?  need to find in between to ignore?
            print('Turn Arounnd')
            boundingCircle(point)
        else:
            go_front()
    if why[0] > .4318:
        print('Go forwards')
        go_front()

    # time.sleep(2)
