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
    u_fit = fitting_function(param_guess, v)
    # Compute the distance between the new and old data sets
    distance = ((u-u_fit)**2).sum()
    return distance

# Function for fitting u as a function of v
def fitting_function(eqn_params, v):
    u = eqn_params[0] + eqn_params[1]*v
    return u

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

# Function to compute the distance between the raw data and the Stationary rail
def DistanceToStationary(data, StLeft_u,StRight_u):
    left_u = data.left_u
    left_v = data.left_v
    right_u = data.right_u
    right_v = data.right_v
    distance = ((left_u-StLeft_u(left_v))**2).sum() + ((right_u-StRight_u(right_v))**2).sum()
    return distance

# Import data
mydata= pd.read_csv("data\\straight-track-points-on-image-1.csv")

# Plot points
#plt.plot(mydata.left_u, mydata.left_v)
#plt.plot(mydata.right_u, mydata.right_v)
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

# Plot the Stationary rail and the current rail
f = plt.figure()
h1, = plt.plot(u_left, v_left, '0.6', label="Stationary rail");
h2, = plt.plot(u_right, v_right, '0.6');
h3, = plt.plot(mydata.left_u, mydata.left_v, 'r', label="Rail 1");
h4, = plt.plot(mydata.right_u, mydata.right_v, 'r');
plt.xlabel('u [px]')
plt.ylabel('v [px]')
plt.legend(handles=[h1,h3]);
#plt.title('13915.953621951565')
plt.gca().invert_yaxis()
plt.show()

# Find u as a function of v for the left and right Stationary rails
u = u_left
v = v_left
InitialParGuess = np.array([-100, -2])

# Fit u as a function of v
fit_result = minimize(lambda param_guess : DataDistance(param_guess, u, v), InitialParGuess)

# Extract fitting parameters and compute best fit
eqn_par_left = [fit_result.x[0], fit_result.x[1]]
StLeft_u = lambda v: fitting_function(eqn_par_left, v)

# Plot the data and the best fit
#f = plt.figure()
#h1, = plt.plot(u, v, label="Left rail raw data");
#h2, = plt.plot(StLeft_u(v), v, label="Left rail fit");
#plt.xlabel('u [px]')
#plt.ylabel('v [px]')
#plt.legend(handles=[h1,h2]);
#plt.gca().invert_yaxis()
#plt.show()

# Find u as a function of v for the left and right Stationary rails
u = u_right
v = v_right
InitialParGuess = np.array([-100, -2])

# Fit u as a function of v
fit_result = minimize(lambda param_guess : DataDistance(param_guess, u, v), InitialParGuess)

# Extract fitting parameters and compute best fit
eqn_par_right = [fit_result.x[0], fit_result.x[1]]
StRight_u = lambda v: fitting_function(eqn_par_right, v)

# Find the distance between the Stationary rail and the current rail
distance = DistanceToStationary(mydata, StLeft_u,StRight_u)
print(distance)