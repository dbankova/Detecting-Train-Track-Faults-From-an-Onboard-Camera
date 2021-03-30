#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:37:03 2021

@author: yz3259
"""


from os import listdir, path

#import numpy as np


def find_path(folders = 'Data'):
    """
    This fun founds the current path and gives a path (mypath) for
    a directed folder.
    """
    dirname = path.dirname(__file__)
    end = len(dirname)- dirname.find("/Codes")
    #print(dirname[0:-end])
    dirname = dirname[0:-end]
    mypath = path.join(dirname, folders)
    #mypath = dirname+folders
    return dirname,mypath


def path_and_files(folders = 'Data'):
    """ This fun gives the path of
    current folder and lists
    all the filenames in the path.
    Input: folders gives
    the relative path of targeted folder.
    """

    dirname,mypath = find_path(folders = folders)
    allfiles = [f for f in listdir(mypath) if path.isfile(path.join(mypath, f))]
    #print(allfiles)
    return dirname, mypath, allfiles

dirname, mypath, allfiles = path_and_files(folders = 'Data/Video')
#image=mpimg.imread('Data/Video/0021700.jpg')