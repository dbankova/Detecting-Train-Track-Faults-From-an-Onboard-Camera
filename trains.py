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


# Import data
mydata= pd.read_csv("data\\straight-track-points-on-image-1.csv")

# Plot points
plt.plot(mydata.left_u, mydata.left_v)
plt.plot(mydata.right_u, mydata.right_v)
plt.gca().invert_yaxis()
plt.show()


u = mydata.left_u
v = mydata.left_v
InitialParGuess = np.array([3, 10])

# Fit v as a function of u
fit_result = minimize(lambda param_guess : DataDistance(param_guess, u, v), InitialParGuess)

# Extract fitting parameters and compute best fit
eqn_par_fit = [fit_result.x[0], fit_result.x[1]]
v_fit = fitting_function(eqn_par_fit, u)

# Plot the data and the best fit
f = plt.figure()
h1, = plt.plot(u, v, label="Left rail raw data");
h2, = plt.plot(u, v_fit, label="Left rail fit");
plt.xlabel('u [px]')
plt.ylabel('v [px]')
plt.legend(handles=[h1,h2]);
plt.gca().invert_yaxis()
plt.show()