import cv2
import os
import numpy as np
from collections import Counter

from PIL import Image
## Read and merge

def find(name,path):
    """
    Finds if the file in a given directory
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root,name)

def mask(filename):
    """
    Applies the mask to the image
    """
    img = cv2.imread(filename)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## Gen lower mask (0-5) and upper mask (175-180) of RED
    mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
    mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))

    ## Merge the mask and crop the red regions
    mask = cv2.bitwise_or(mask1, mask2 )
    croped = cv2.bitwise_and(img, img, mask=mask)
    
    mask_name = filename+'_mask'+'.jpg'
    
    cv2.imwrite(mask_name, croped)
    
    return mask_name

def pixels(mask_file,month_pixels):
    img = Image.open(mask_file)
    width, height = img.size
    
    for i in range(width):
        for j in range(height):
            pixel_location = str([i,j])
            rgb_pixel_value = img.getpixel((i,j)) 
            if rgb_pixel_value != (0,0,0):
                month_dict(month_pixels, pixel_location)
                #month_pixels.append([i,j])
                
def month_dict(month_pixels,pix_loc):
    # if the same pixel location has occured update to occurance counter
    if pix_loc in month_pixels.keys():
        updated = {pix_loc : (int(month_pixels[pix_loc]) + 1)}
        month_pixels.update(updated)
    
    # creating the first instance of the pixel counter
    else:
        month_pixels[pix_loc] = 1


def main(Year, Month, Day):
    month_pixels = {
            }        
    for d in Day:
        file = str(d) + str(Month) + str(Year) + '.jpg'
        path = 'C://Users/Dan/Documents/SpaceScienceAndTechnologyMasters/Project/Data/UCD_Project/'
        filename = find(file,path)
        try:
            final_mask = mask(filename)
            pixels(final_mask,month_pixels)
                    
        except (OSError, KeyError) as e:
            pass
                 
    return month_pixels