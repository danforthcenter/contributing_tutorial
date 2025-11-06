# Dummy versioning
# __version__ = "0.0.1"

from littlecv.littlecv.analyze_size import size
from littlecv.littlecv.outputs import Outputs
from littlecv.littlecv.readimage import readimage
from littlecv.littlecv.rgb2gray_lab import rgb2gray_lab
from littlecv.littlecv.threshold_binary import binary
from littlecv.littlecv.fill import fill
from littlecv.littlecv.plot_image import plot_image

__all__ = [
    "analyze_size",
    "Outputs",
    "readimage",
    "rgb2gray_lab",
    "binary",
    "fill",
    "plot_image"
]
