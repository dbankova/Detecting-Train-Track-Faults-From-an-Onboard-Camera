# -*- coding: utf-8 -*-
"""
UK Graduate Modelling Camp 29-31 March 2021:
Detecting Train Track Faults From an Onboard Camera
"""
#Code for looking at train tracks from camera images
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import data - file location needs changing
mydata= pd.read_csv("data\\straight-track-points-on-image-1.csv")

#plot points
plt.plot(mydata.left_u,mydata.left_v)
plt.plot(mydata.right_u,mydata.right_v)
plt.show()
