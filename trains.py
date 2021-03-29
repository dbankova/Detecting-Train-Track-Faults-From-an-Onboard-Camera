# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:05:47 2021
#Hello???
@author: dob1u19
"""
#Code for looking at train tracks from camera images
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import data - file location needs changing
mydata= pd.read_csv("C:\\Users\\Deepanshu\\Documents\\file1.csv")

#plot points
plt.plot(mydata.left_u,mydata.left_v)
plt.plot(mydata.right_u,mydata.right_v)
plt.show()
