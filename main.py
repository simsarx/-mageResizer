from PIL import Image
import glob
import os
img_dir = "C:/Users/Muhammet.ORHAN/Desktop/Python/İmageResizer/product/"
dirs = os.listdir(img_dir)



def resize_bulk_images():
    for img in dirs:
        if os.path.isfile(img_dir + img):
            im = Image.open(img_dir + img)
            imageWidth =int(round(im.size[0]*0.4)) 
            image_height =int(round(im.size[1]*0.4)) 
            
            print(int(im.size[0])-imageWidth,int(im.size[1])-image_height)
            
       
            f, e = os.path.splitext(img_dir + img)
            imResize = im.resize((imageWidth,imageWidth), Image.ANTIALIAS)
            imResize.save(f + '_resized.webp', quality=100)
            
            
print('Bulk images resizing started...')


resize_bulk_images()


print('Bulk images resizing finished...')