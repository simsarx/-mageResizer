from PIL import Image
import glob
import os
img_dir = "C:/Users/Muhammet.ORHAN/Desktop/Python/İmageResizer/GWD/"
dirs = os.listdir(img_dir)


def resize_bulk_images():
    for img in dirs:
        if os.path.isfile(img_dir + img):
            im = Image.open(img_dir + img)
            imageWidth = int(round(im.size[0]*0.5))
            image_height = int(round(im.size[1]*0.5))

            print(int(im.size[0])-imageWidth, int(im.size[1])-image_height)

            f, e = os.path.splitext(img_dir + img)
            imResize = im.resize((imageWidth, image_height), Image.ANTIALIAS)
            imResize.save(f + '_resized.png', quality=100)


print('Bulk images re-structure started...')


resize_bulk_images()


print('Bulk images re-structure finished...')
