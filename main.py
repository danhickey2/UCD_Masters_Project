import cv2
import mask
import os

import ImageCreator
import numpy as np

from collections import Counter
from PIL import Image


def main():
    
    blank_image = 'Blank.jfif'
    
    
    Day = ['01','02','03','04','05','06','07','08','09','10','11','12','13',
           '14','15','16','17','18','19','20','21','22','23','24','25','26',
           '27','28','29','30','31']
    """
    
    
    """
    
    Month = ['Jan' , 'Feb' , 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept','Oct', 'Nov', 'Dec'] 
    # 'August', 'October'
    #'Jan' , 'Feb' , 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept','Oct', 'Nov', 'Dec'
    
    Year = ['2017','2018','2019'] # '2013','2014','2015','2016','2017','2018','2019'
    
    for y in Year:
        for m in Month:
            freq = mask.main(y, m, Day)
            image_name =str(m) + str(y) + 'Frequency.jpg'
            
            ImageCreator.frequencyImage(blank_image,freq,image_name)
        
    
main()