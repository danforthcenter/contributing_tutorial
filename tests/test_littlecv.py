import os
from littlecv import littlecv as lcv


def test_littlecv_workflow():
    """Test for your edit"""
    data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata/plant_cropped.png")
    img, _, _ = lcv.readimage(filename=data, plot=False)
    b_img = lcv.rgb2gray_lab(rgb_img=img, channel='b', plot=False)
    thresh_mask = lcv.binary(gray_img=b_img, threshold=130, object_type='light', plot=False)
    fill_mask = lcv.fill(thresh_mask, size=1000, plot=False)
    _, outputs = lcv.size(img=img, mask=fill_mask, plot=False)
    
    assert outputs.observations["littlecv_test"]["area"]["value"] == 198568.0
