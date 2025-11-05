# Read image
import os
import cv2
import numpy as np


def readimage(filename):
    """Read image from file. Simplified from plantcv.plantcv.readimage for littlecv

    Parameters
    ----------
    filename = str, name of image file

    Returns
    -------
    img      = numpy.ndarray, image object as numpy array
    path     = str, path to image file
    img_name = str, name of image file
    """

    img = cv2.imread(filename, -1)
    # Default to drop alpha channel if user doesn't specify 'rgba'
    if len(np.shape(img)) == 3 and np.shape(img)[2] == 4:
        img = cv2.imread(filename)

    if img is None:
        raise RuntimeError("Failed to open" + filename)

    # Split path from filename
    path, img_name = os.path.split(filename)

    return img, path, img_name
