import os
import cv2
import matplotlib
import numpy as np
from littlecv import littlecv as lcv


# disable plotting
matplotlib.use("Template")


def test_readimage():
    """Test littlecv readimage"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    assert img.shape == (2000, 1600, 3)


def test_plot_image():
    """Test littlecv plot_image"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    lcv.plot_image(img)
    assert True

    
def test_rgb2gray():
    """Test littlecv rgb to grayscale conversion"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    b_img = lcv.rgb2gray_lab(rgb_img=img, channel='b', plot=False)
    assert b_img.shape == (2000, 1600)


def test_binary():
    """Test littlecv binary threshold"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    b_img = lcv.rgb2gray_lab(rgb_img=img, channel='b', plot=False)
    thresh_mask = lcv.binary(gray_img=b_img, threshold=130, plot=False)
    assert all(np.unique(thresh_mask) == [0, 255])


def test_fill():
    """Test littlecv fill"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    b_img = lcv.rgb2gray_lab(rgb_img=img, channel='b', plot=False)
    thresh_mask = lcv.binary(gray_img=b_img, threshold=130, plot=False)
    fill_mask = lcv.fill(thresh_mask, size=1000, plot=False)
    assert np.sum(fill_mask) < np.sum(thresh_mask)


def test_area():
    """Test littlecv size"""
    d = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0,1,1,1,0], [0, 0, 1, 0, 0]]).astype("uint8")
    _, out = lcv.size(img=d, mask=d)
    assert out.observations["littlecv_test"]["area"]["value"] == np.sum(d)


def test_littlecv_workflow():
    """Test for your edit"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    b_img = lcv.rgb2gray_lab(rgb_img=img, channel='b', plot=False)
    thresh_mask = lcv.binary(gray_img=b_img, threshold=130, plot=False)
    fill_mask = lcv.fill(thresh_mask, size=1000, plot=False)
    _, outputs = lcv.size(img=img, mask=fill_mask, plot=False)
    assert outputs.observations["littlecv_test"]["area"]["value"] == 198568.0
