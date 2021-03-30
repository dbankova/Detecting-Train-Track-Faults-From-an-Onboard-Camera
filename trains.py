# -*- coding: utf-8 -*-
"""
UK Graduate Modelling Camp 29-31 March 2021:
Detecting Train Track Faults From an Onboard Camera
"""
# Code for looking at train tracks from camera images
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Function to compute the distance between the raw data and the best estimate
def DataDistance(param_guess, u, v):
    # Check that the raw data has the correct length
    assert u.shape == v.shape, \
        "The number of u-coordinates {} is not ".format(u.shape) \
        + "equal to the number of v-coordinates {}".format(v.shape)
    # Compute v_fit = param_guess[0] + param_guess[1]*u
    v_fit = fitting_function(param_guess, u)
    # Compute the distance between the new and old data sets
    distance = ((v-v_fit)**2).sum()
    return distance

# Function for fitting v as a function of u
def fitting_function(eqn_params, u):
    v = eqn_params[0] + eqn_params[1]*u
    return v

# Transformation matrix from real 3D space to 2D image space
def transformation_matrix(f, angles, coordinates, campos):
    theta,phi,psi = angles
    # Rotation matrices
    R1 = np.matrix([[ 1, 0           , 0           ],
                   [ 0, np.cos(psi), np.sin(psi)],
                   [ 0, -np.sin(psi), np.cos(psi)]])
    R2 = np.matrix([[ np.cos(theta), 0, -np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [ np.sin(theta), 0, np.cos(theta)]])
    R3 = np.matrix([[ np.cos(phi), np.sin(phi), 0 ],
                   [ -np.sin(phi), np.cos(phi) , 0 ],
                   [ 0           , 0            , 1 ]])
    new_coords = np.dot(np.dot(R1,np.dot(R2,R3)),coordinates-campos)
    if new_coords[0,0] == 0:
        return np.array([0,0])
    return f*np.array([new_coords[0,1],new_coords[0,2]])/new_coords[0,0]

# Import data
mydata= pd.read_csv("data\\straight-track-points-on-image-1.csv")

# Plot points
plt.plot(mydata.left_u, mydata.left_v)
plt.plot(mydata.right_u, mydata.right_v)
plt.gca().invert_yaxis()
plt.show()

#u = mydata.left_u
#v = mydata.left_v
#InitialParGuess = np.array([-100, -2])

# Fit v as a function of u
#fit_result = minimize(lambda param_guess : DataDistance(param_guess, u, v), InitialParGuess)

# Extract fitting parameters and compute best fit
#eqn_par_fit = [fit_result.x[0], fit_result.x[1]]
#v_fit = fitting_function(eqn_par_fit, u)

# Plot the data and the best fit
#f = plt.figure()
#h1, = plt.plot(u, v, label="Left rail raw data");
#h2, = plt.plot(u, v_fit, label="Left rail fit");
#plt.xlabel('u [px]')
#plt.ylabel('v [px]')
#plt.legend(handles=[h1,h2]);
#plt.gca().invert_yaxis()
#plt.show()

g = 1.435 # track gauge
w = 0.11 # track width
h = 2.165 # camera height
f = 0.0058 # focal length

# Camera position in 3D space
campos = np.array([0,0.6,-2.165])

# theta (the pitch angle), phi (yaw angle) and psi (the roll angle)
angles = np.array([-0.3333578871,-0.1270599695,0])

# Number of data points to generate
n = 50
# Generate left rail when stationary
left_rail_3D = np.array([np.linspace(5, 20, num = n), -g/2*np.ones(n), np.zeros(n)])
left_rail_3D = np.transpose(left_rail_3D)
u_left = np.zeros(n)
v_left = np.zeros(n)
for i in range(n):
    u_left[i],v_left[i] = transformation_matrix(f, angles, left_rail_3D[i], campos)*181818.1818

# Generate right rail when stationary
right_rail_3D = np.array([np.linspace(5, 20, num = n), g/2*np.ones(n), np.zeros(n)])
right_rail_3D = np.transpose(right_rail_3D)
u_right = np.zeros(n)
v_right = np.zeros(n)
for i in range(n):
    u_right[i],v_right[i] = transformation_matrix(f, angles, right_rail_3D[i], campos)*181818.1818

# Plot left and right rail
f = plt.figure()
h1, = plt.plot(u_left, v_left, label="Left rail");
h2, = plt.plot(u_right, v_right, label="Right rail");
h3, = plt.plot(mydata.left_u, mydata.left_v, label="Left rail 1");
h4, = plt.plot(mydata.right_u, mydata.right_v, label="Right rail 1");
plt.xlabel('u [px]')
plt.ylabel('v [px]')
plt.legend(handles=[h1,h2,h3,h4]);
plt.gca().invert_yaxis()
plt.show()
