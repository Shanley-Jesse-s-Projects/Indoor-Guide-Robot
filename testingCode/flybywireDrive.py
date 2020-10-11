#this module doesn't work yet. "no module named keyboard"

import keyboard #supposed to import module
import L2_speed_control as sc       #imports open loop speed control
import L1_motors as m               #imports use of the motors


def drive(pdl, pdr):        #generic drive function which takes in the speeds only
    duties = sc.openLoop(pdl, pdr) # produce duty cycles from the phi dots
    m.MotorL(duties[0]) # send command to motors
    m.MotorR(duties[1]) # send command to motors
    
def forward():      #feeds commands to drive the motors forward
    drive(7.7, 7.7)
def backward():     #feeds commands to drive the motors backward
    drive(-7.7, -7.7)   
def left():          #feeds commands to drive the motors left
    drive-(7.7, 7.7)
def right():         #feeds commands to drive the motors right
    drive(7.7, -7.7)
    
while(1):
    if keyboard.is_pressed('w'):
        forward()
        break
    if keyboard.is_pressed('s'):
        backward()
        break
    if keyboard.is_pressed('a'):
        left()
        break
    if keyboard.is_pressed('d'):
        right()
        break
