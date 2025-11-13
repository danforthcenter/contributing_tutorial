import cv2
from littlecv.littlecv.plot_image import plot_image


def binary(gray_img, threshold, plot=True):
    """Creates a binary image from a grayscale image based on the threshold value.

    Inputs:
    gray_img     = numpy.ndarray, Grayscale image data
    threshold    = int, Threshold value (0-255)
    plot         = bool, lazy version of pcv.params.debug

    Returns:
    bin_img      = numpy.ndarray, Thresholded binary image
    """
    # Threshold the image
    _, bin_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)

    plot_image(bin_img, plot=plot)

    return bin_img
