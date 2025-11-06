import cv2
from littlecv.littlecv.plot_image import plot_image


def binary(gray_img, threshold, object_type="light", plot=True):
    """Creates a binary image from a grayscale image based on the threshold value.

    Inputs:
    gray_img     = numpy.ndarray, Grayscale image data
    threshold    = int, Threshold value (0-255)
    object_type  = str, "light" or "dark" (default: "light")
                   - If object is lighter than the background then standard thresholding is done
                   - If object is darker than the background then inverse thresholding is done
    plot         = bool, lazy version of pcv.params.debug

    Returns:
    bin_img      = numpy.ndarray, Thresholded binary image
    """
    # Set the threshold method
    threshold_method = ""
    if object_type.upper() == "LIGHT":
        threshold_method = cv2.THRESH_BINARY
    elif object_type.upper() == "DARK":
        threshold_method = cv2.THRESH_BINARY_INV
    else:
        RuntimeError('Object type ' + str(object_type) + ' is not "light" or "dark"!')

    # Threshold the image
    _, bin_img = cv2.threshold(gray_img, threshold, 255, threshold_method)

    plot_image(bin_img, plot=plot)

    return bin_img
