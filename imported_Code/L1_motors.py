#NOT OUR CODE. BASE File PROVIDED THROUGH THE MXET 300 CLASS
#FILE ADAPTED FROM ORIGINAL 
# This example drives the right and left motors.
# Intended for Beaglebone Blue hardware.
# This example uses rcpy library. Documentation: guitar.ucsd.edu/rcpy/rcpy.pdf

import rcpy
import rcpy.motor as motor
import time # only necessary if running this program as a loop
#import random

motor_l = 1 	# Left Motor
motor_r = 2 	# Right Motor

rcpy.set_state(rcpy.RUNNING) # initialize the rcpy library

# define functions to command motors, effectively controlling PWM
def MotorL(speed): # takes argument in range [-1,1]
    motor.set(motor_l, speed)
    #time.sleep(2)

def MotorR(speed): # takes argument in range [-1,1]
    motor.set(motor_r, speed)
    #time.sleep(2)

# Uncomment this section to run this program as a standalone loop
#while rcpy.get_state() != rcpy.EXITING: # exit loop if rcpy not ready
 #   if rcpy.get_state() == rcpy.RUNNING: # execute loop when rcpy is ready
  #       print("L1_motors.py: driving fwd")
        #  MotorL(random.uniform(.4, 1))  # gentle speed for testing program. 0.3 PWM may not spin the wheels.
        #  MotorR(random.uniform(.4, 1))
        # time.sleep(4) # run fwd for 4 seconds
   #      print("L1_motors.py: driving reverse")
    #     MotorL(0.65)
     #    MotorR(.5)
      #   time.sleep(4) # run reverse for 2 seconds
        # MotorL(-0.65)
        # MotorR(-0.5)
# while(1):
#  MotorL(-0.65)
#  MotorR(-0.5)


def threadMot():
 MotorL(1)
 MotorR(1)
 
