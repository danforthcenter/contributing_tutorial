# Read image
import os
import cv2
import numpy as np
from littlecv.littlecv.plot_image import plot_image


def readimage(filename, plot=True):
    """Read image from file. Simplified from plantcv.plantcv.readimage for littlecv

    Parameters
    ----------
    filename = str, name of image file
    plot     = bool, lazy version of pcv.params.debug

    Returns
    -------
    img      = numpy.ndarray, image object as numpy array
    path     = str, path to image file
    img_name = str, name of image file
    """

    img = cv2.imread(filename, -1)
    # Split path from filename
    path, img_name = os.path.split(filename)
    # we are always going to debug in this dummy version
    plot_image(img, plot=plot)
    
    return img, path, img_name
