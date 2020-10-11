#This code was written by: Shanley Mullen
#email: shanleymullen@gmail.com

L2_vector as vector #the imported file was provided through the MXET 300 class. 
import numpy as np
from math import *


# The purpose of this code is to be able to find the P2 value in front of the lidar, this was to be used in a bounding square
#we changed this to a bounding circle after this initial version

# Make a function for point 1 from the initial lidar point
def x(whole):
    for i in whole:
        m = np.array(whole)
    B = m[0]
    C = m[1]
    dx_1 = np.cos(C)
    dx = np.dot(dx_1, B)
    return dx


def y(whole):
    for i in whole:
        m = np.array(whole)
    B = m[0]
    C = m[1]
    dy_1 = np.sin(C)
    dy = np.dot(dy_1, B)
    return dy


def P_1x(dx, dy, whole):
    theta = 1.57
    ang = np.arctan(dy / dx)
    d_1 = np.sin(theta)
    d_2 = np.cos(ang)
    P_Px = np.dot(d_1, d_2)
    return P_Px


def P_1y(dx, dy, whole):
    theta = 1.57
    ang = np.arctan(dy / dx)
    d_1 = np.sin(theta)
    d_2 = np.sin(ang)
    P_Py = np.dot(d_1, d_2)
    return P_Py


# make a function to do the calculations
def lidar_mathx(dx, P_P, P_0, whole):
    p1 = P_P - P_0
    x_p_2 = dx + p1
    P_x2 = np.mean(x_p_2)
    return P_x2


def lidar_mathy(dy, P_P, P_0, whole):
    p1 = P_P - P_0
    p_y_2 = dy + p1
    P_y2 = np.array(p_y_2)
    P_y2 = np.mean(P_y2)
    return P_y2


def x_global(whole, x_1, P_Py, P_Px, P_x2, P_y2):
    for i in whole:
        m = np.array(whole)
    ang = np.arctan(P_y2 / P_x2)
    no = np.cos(ang)
    no = np.dot(no, P_Px)
    yes = np.sin(P_Py / P_Px)
    yes = np.dot(yes, P_Py)
    x_g2 = yes - no + x_1
    return x_g2


def y_global(whole, y_1, P_Py, P_Px, P_x2, P_y2):
    for i in whole:
        m = np.array(whole)
    ang = np.arctan(P_y2 / P_x2)
    no = np.sin(ang)
    no = np.dot(no, P_Px)
    yes = np.cos(P_Py / P_Px)
    yes = np.dot(yes, P_Py)
    y_g2 = yes + no + y_1
    return y_g2


def dArea(dx, dy, y):  # only depends on dx and dy updating.
    print("dx: ", dx, "dy: ", dy)  #
    # finds the area
    a = abs(pi * whole[0])
    return (a)

# Set the initial values here
global P_0
P_0 = [.1651, .0254]  # the values for the location of the lidar on the robot
maybe = []
i = 0
# Call the main function, use for standalone function
# while(1):
#   whole = vector.getNearest()
#  print('Initial Points: ', whole)
# x_int = x(whole)
# y_int = y(whole)
#    print()
#   lidar_x = lidar_mathx(x_int, P_1x(x_int, y_int ,whole), P_0, whole)
#  lidar_y = lidar_mathy(y_int, P_1y(x_int, y_int ,whole), P_0, whole)
# one = P_1x(x_int, y_int ,whole)
#    two = P_1y(x_int, y_int ,whole)
# #Make sure that the values are 'good' AKA that there is nothing else present
# #From there stack the data and save the points
#   if whole[0] > .4318:
#      print('X Value Point 2 Local: ', lidar_x)
#     print()
#    print('Y Value Point 2 Local: ', lidar_y)
#   print()
#  x_g = x_global(x_int, y_int,one, lidar_x, lidar_y)
# y_g = y_global(x_int, y_int, two,one, lidar_x, lidar_y)
#    print('X Value Point 2 Global: ', x_g)
#   print()
#  print('Y Value Point 2 Global: ', y_g)
# print()
#    lidar_coord = np.array([lidar_x, lidar_y])
#   print()
#  maybe.append(lidar_coord)
# if whole[0] > .4318:
# i += 1
#    if i > 2:
#       ar=dArea(x_int, y_int, whole[0])
#      print('Area: ', ar)
#    print()
#   print(i)
# time.sleep(2)
# i += 1
#    time.sleep(2)
