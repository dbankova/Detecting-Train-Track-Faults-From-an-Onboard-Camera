#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:32:50 2021

@author: yz3259
"""
#import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
import matplotlib.image as mpimg

from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
from skimage.feature import canny

# Line finding using the Probabilistic Hough Transform
#image = data.camera()


def hough_transform(image_file,input_path,output_path,canny_par=(5,5,26),image_num = 1):
    """
    This fun load in a image and perform the hough transformation.
    Output: hough transformation images
            Parameters

    """
    #load in data
    image=mpimg.imread(input_path+f'/{image_file}')
    image = image[:,:,0]
    edges = canny(image, canny_par[0],canny_par[1],canny_par[2])
    lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                     line_gap=3)

    if image_num ==3:
        # Generating figure
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
        ax = axes.ravel()

        ax[0].imshow(image, cmap=cm.gray)
        ax[0].set_title('Input image')

        ax[1].imshow(edges, cmap=cm.gray)
        ax[1].set_title('Canny edges')

        ax[2].imshow(edges * 0)
        for line in lines:
            p0, p1 = line
            ax[2].plot((p0[0], p1[0]), (p0[1], p1[1]))

        ax[2].set_xlim((0, image.shape[1]))
        ax[2].set_ylim((image.shape[0], 0))
        ax[2].set_title('Probabilistic Hough')

        for a in ax:
            a.set_axis_off()

        plt.tight_layout()
        plt.savefig(output_path+f'/houghTrans_pairs{image_num}_{image_file[:-4]}.png')
   # extent = ax[2].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #fig.savefig('Data/Output/ax2_figure.png', bbox_inches=extent)
        #plt.show()
        plt.close()
    elif image_num ==2:
        ig, axes = plt.subplots(1, 2, figsize=(20, 10), sharex=True, sharey=True)
        ax = axes.ravel()

        ax[0].imshow(image, cmap=cm.gray)
        ax[0].set_title('Input image')

        ax[1].imshow(edges * 0)
        for line in lines:
            p0, p1 = line
            ax[1].plot((p0[0], p1[0]), (p0[1], p1[1]))

        ax[1].set_xlim((0, image.shape[1]))
        ax[1].set_ylim((image.shape[0], 0))
        ax[1].set_title('Probabilistic Hough')

        for a in ax:
            a.set_axis_off()

        plt.tight_layout()
        plt.savefig(output_path+f'/houghTrans_pairs{image_num}_{image_file[:-4]}.png')
   # extent = ax[2].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #fig.savefig('Data/Output/ax2_figure.png', bbox_inches=extent)
        #plt.show()
        plt.close()
    elif image_num ==1:
        ig, ax = plt.subplots(1, 1, figsize=(10, 10), sharex=True, sharey=True)
        ax = axes.ravel()

      #  ax[0].imshow(image, cmap=cm.gray)
       # ax[0].set_title('Input image')

        ax.imshow(edges * 0)
        for line in lines:
            p0, p1 = line
            ax.plot((p0[0], p1[0]), (p0[1], p1[1]))

        ax.set_xlim((0, image.shape[1]))
        ax.set_ylim((image.shape[0], 0))
        ax.set_title('Probabilistic Hough')

        for a in ax:
            a.set_axis_off()

        plt.tight_layout()
        plt.savefig(output_path+f'/houghTrans_{image_file[:-4]}.png')
   # extent = ax[2].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #fig.savefig('Data/Output/ax2_figure.png', bbox_inches=extent)
        #plt.show()
        plt.close()
        return 'Ok!'
