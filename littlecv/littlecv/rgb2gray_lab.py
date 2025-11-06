import os
import cv2
from littlecv.littlecv.plot_image import plot_image


def rgb2gray_lab(rgb_img, channel, plot=True):
    """Convert image from RGB colorspace to LAB colorspace.
    Returns the specified subchannel as a gray image.
    Simplified from plantcv.plantcv.rgb2gray_lab for littlecv

    Parameters
    ----------
    rgb_img : numpy.ndarray
        RGB image data
    channel : str
        color subchannel (l = lightness, a = green-magenta, b = blue-yellow)
    plot    : bool
        lazy version of pcv.params.debug
    
    Returns
    -------
    numpy.ndarray
        grayscale image from one LAB color channel
    """
    # Convert RGB to LAB and return the specified subchannel as a gray image
    gray_img = _rgb2lab(rgb_img=rgb_img, channel=channel)

    # The allowable channel inputs are l, a or b
    names = {"l": "lightness", "a": "green-magenta", "b": "blue-yellow"}

    plot_image(gray_img, plot=plot)

    return gray_img


def _rgb2lab(rgb_img, channel):
    """Convert image from RGB colorspace to LAB colorspace.
    Returns the specified subchannel as a gray image.
    Simplified from plantcv.plantcv._helpers._rgb2lab for littlecv

    Parameters
    ----------
    rgb_img : numpy.ndarray
        RGB image data
    channel : str
        color subchannel (l = lightness, a = green-magenta, b = blue-yellow)

    Returns
    -------
    numpy.ndarray
        grayscale image from one LAB color channel
    """
    channel = channel.lower()
    # Convert the input BGR image to LAB colorspace
    lab = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2LAB)
    # Split LAB channels
    l, a, b = cv2.split(lab)
    # Create a channel dictionaries for lookups by a channel name index
    channels = {"l": l, "a": a, "b": b}
    return channels[channel]
