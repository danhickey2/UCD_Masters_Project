# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:16:34 2020

@author: Dan
"""
import cv2
import numpy as np

def frequencyImage(blank_image, month_frequency,image_name):  
    image = cv2.imread(blank_image)
    for key in month_frequency.keys():
        step1 = key.strip('[]')
        
        #the x and y are switched for some reason
        key_x = int(step1.split(',')[0])
        key_y = int(step1.split(',')[1])
        # between 1-7 occurences change the pixel colour to red
        
        if month_frequency[key] >= 1 and month_frequency[key] <= 7:
            #[key_y,key_x] [key_x, key_y]
            image[key_y,key_x] = (0,0,255) 
        
        # between 8-14 occurences change the pixel colour to orange
        if month_frequency[key] >= 8 and month_frequency[key] <= 14:
            image[key_y,key_x] = (0,128,255)
        
        # between 15-22 occurences change the pixel colour to yellow
        if month_frequency[key] >= 15 and month_frequency[key] <= 22:
            image[key_y,key_x] = (0,255,255)
            
        # between 23-31 occurences change the pixel colour to green
        if month_frequency[key] >= 23 and month_frequency[key] <= 31:
            image[key_y,key_x] = (51,255,51)
            
    
    cv2.imwrite(image_name,image)
    