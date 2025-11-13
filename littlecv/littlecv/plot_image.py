"""Plot image to screen."""
import cv2
import numpy
import matplotlib
from matplotlib import pyplot as plt


def plot_image(img, cmap=None, plot=True, **kwargs):
    """
    Plot an image to the screen.

    :param img: numpy.ndarray, ggplot, xarray.core.dataarray.DataArray
    :param cmap: str
    :param plot: bool, make a plot
               (defaults True, only used internally in place of pcv.params.debug)
    :param kwargs: key-value arguments to xarray.plot method
    :return:
    """
    dimensions = numpy.shape(img)

    if isinstance(img, numpy.ndarray) and plot:
        matplotlib.rcParams['figure.dpi'] = 100
        # If the image is color then OpenCV stores it as BGR, we plot it as RGB
        if len(dimensions) == 3:
            plt.figure()
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
