from PIL import Image
import sys

def processImage(file):
    try:
        im = Image.open(file)
    except IOError:
        print('Cannot load ', file)
        sys.exit(1)
    i = 0
    palette = im.getpalette()
    
    try: 
        while True:
            im.putpalette(palette)
            new_im = Image.new('RGB', im.size)
            new_im.paste(im)
            new_im.save(str(i) + 'Jan2013.png')
            
            i+=1
            im.seek(im.tell() + 1)
    
    except EOFError:
        pass
    
    
processImage('Jan2013.gif')