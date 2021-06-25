# importing the Modules
import cv2
import numpy as np
import matplotlib.pyplot as plt


# flag methods¶
"""
https://docs.opencv.org/4.5.2/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80

"""

# Facing some issues with Jupyter so moving to VS code



def read_img(path, flags = None):
    """
    doc : Read an image
    path :: Path to the file
    flags :: the method to open the files
    """
    return cv2.imread(path, flags)


def show_img_cv2(window_name, img):
    """
    doc : Show an image in cv2 window
    window_name :: name of the window 
    img :: The image to show 
    """
    cv2.imshow(window_name, img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    

def show_img_matplotlib(img):
    """
    doc : Show an image in matplotlib
    img :: The image to show 
    """
    plt.imshow(img)
    plt.show()

    
def write_img(path, img):
    """
    doc : Write and save an image
    path :: Path to the file
    img :: The image to write 
    """
    cv2.imwrite(path, img)



def main():
    img = read_img('assets/messi.jpeg')
    show_img_cv2('messi',img)
    show_img_matplotlib(img)
    write_img('output/messi.jpeg', img)



if __name__ =='__main__':
    main()

    