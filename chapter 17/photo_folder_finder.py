import os
from PIL import Image


for foldername, subfolders, filenames in os.walk('.'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith('jpg') or filename.lower().endswith('png'):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im=Image.open(os.path.join(foldername,filename))
        width,height=im.size

        # Check if width & height are larger than 500.
        if width>500 and height>500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    if numPhotoFiles>numNonPhotoFiles:
        print(os.path.abspath(foldername))
    else:
        print('There are no photo folders,do you want to find folders with at least a quarter images in it?(yes or no)')
        answer=input()
        if answer=='yes':
            if numPhotoFiles>numNonPhotoFiles:
                print(os.path.abspath(foldername))
            else:
                print('These are files that contain few photos, there are no photofolders here!')
    # print the absolute path of the folder.
    

