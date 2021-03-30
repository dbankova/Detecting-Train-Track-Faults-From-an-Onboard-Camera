#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:20:21 2021

@author: yz3259
"""

#import numpy as np

import files_paths as fp
import houghTransform as ht

_, input_path, allfiles = fp.path_and_files(folders = 'Data/Video')
_, output=fp.find_path(folders = 'Data/Output')

for image in allfiles:
    ht.hough_transform(image,input_path,output,canny_par=(5,5,26),image_num = 2)
