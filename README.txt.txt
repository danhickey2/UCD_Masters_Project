> Gif_to_jpg.py
This script imports the gif file created by EO Browser and separates each frame into an image, saving and naming them depenedent on what frame is saved.

> ImageCreator.py
Takes the dictionary output from mask.py and uses the key values to assign a pixel colour to the image based on the number of fire occurences in a month. 1-7: red, 8-14: orange, 15-22: yellow, 23-31: green

> mask.py 
This script searches for the red pixels within the image and creates a mask to isolate them. The script saves the position of each red pixel in a dictionary. This process is repeated for each image in a month. If a fire occurs in the same pixel as a previous image, the key is updated to account for the frequency

> mainpy
Calls the mask.py and ImageCreator.py scripts

****
Final Image:
Contains the compiled monthly images

****
2013,2014...
Contains the images for the respective year