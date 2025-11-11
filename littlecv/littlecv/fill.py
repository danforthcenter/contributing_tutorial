# Object fill device

import numpy as np
import numpy as np
from littlecv.littlecv.plot_image import plot_image
from skimage.morphology import remove_small_objects


def fill(bin_img, size, plot=True):
    """Identifies objects and fills objects that are less than size.

    Inputs:
    bin_img      = Binary image data
    size         = minimum object area size in pixels (integer)
    plot         = bool, lazy version of pcv.params.debug

    Returns:
    filtered_img = image with objects filled

    :param bin_img: numpy.ndarray
    :param size: int
    :return filtered_img: numpy.ndarray
    """
    # Cast binary image to boolean
    bool_img = bin_img.astype(bool)

    bool_img = remove_small_objects(bool_img, min_size=size)
    # Cast boolean image to binary and make a copy of the binary image for returning
    filtered_img = np.copy(bool_img.astype(np.uint8) * 255)

    plot_image(filtered_img, plot=plot)

    return filtered_img
