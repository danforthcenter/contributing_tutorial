"""Analyzes the shape and size of objects and outputs data."""
import os
import cv2
import numpy as np
from littlecv.littlecv.outputs import Outputs
from littlecv.littlecv.plot_image import plot_image


def size(img, mask, label="littlecv_test", plot=True):
    """A function that analyzes the shape and size of objects and outputs data.

    Inputs:
    img          = numpy.ndarray, RGB image data for plotting
    mask         = numpy.ndarray, mask of object (32-bit).
    label        = str, Optional label parameter, modifies the variable name of
                   observations recorded (default = pcv.params.sample_label).
    plot         = bool, lazy version of pcv.params.debug

    Returns:
    outputs        = dict, dictionary of outputs
    analysis_image = numpy.ndarray, Diagnostic image showing measurements.
    """
    img, outputs = _analyze_size(img=img, mask=mask, label=label)

    plot_image(img, plot=plot)

    return img, outputs


def _analyze_size(img, mask, label):
    """Analyze the size of individual objects.

    Inputs:
    img   = RGB image data for plotting
    mask  = Binary image data
    label = Label of object

    Returns:
    analysis_image = Diagnostic image showing measurements

    :param mask: numpy.ndarray
    :param label: int
    :return analysis_image: numpy.ndarray
    """
    # initialize outputs container
    outputs = Outputs()

    # Initialize analysis output values
    area = 0
    hull_area = 0
    solidity = 0
    perimeter = 0
    total_edge_length = 0
    width = 0
    height = 0
    caliper_length = 0
    longest_path = 0
    cmx = 0
    cmy = 0
    hull_vertices = 0
    ellipse_center = 0, 0
    ellipse_major_axis = 0
    ellipse_minor_axis = 0
    ellipse_angle = 0
    ellipse_eccentricity = 0
    # Check is object is touching image boundaries (QC)
    in_bounds = True

    # Plot image
    plt_img = np.copy(img)

    # Find contours
    cnt, cnt_str = cv2.findContours(np.copy(mask), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2:]

    # Consolidate contours
    obj = _object_composition(contours=cnt, hierarchy=cnt_str)

    # Analyze shape properties if the object is large enough
    if len(obj) > 5:
        # Convex Hull
        hull = cv2.convexHull(obj)
        # Number of convex hull vertices
        hull_vertices = len(hull)
        # Convex Hull area
        hull_area = cv2.contourArea(hull)
        # Moments
        m = cv2.moments(mask, binaryImage=True)
        # Area
        area = m['m00']
        # Solidity
        solidity = area / hull_area if hull_area != 0 else 1
        # Perimeter
        perimeter = cv2.arcLength(obj, closed=True)
        # Total edge legnth
        for contour in cnt:
            total_edge_length += cv2.arcLength(contour, True)
        # Bounding rectangle
        x, y, width, height = cv2.boundingRect(obj)
        # Centroid/Center of Mass
        cmx = m['m10'] / m['m00']
        cmy = m['m01'] / m['m00']
        # Bounding ellipse
        ellipse_center, axes, ellipse_angle = cv2.fitEllipse(obj)
        major_axis_idx = np.argmax(axes)
        minor_axis_idx = 1 - major_axis_idx
        ellipse_major_axis = float(axes[major_axis_idx])
        ellipse_minor_axis = float(axes[minor_axis_idx])
        ellipse_eccentricity = float(np.sqrt(1 - (axes[minor_axis_idx] / axes[major_axis_idx]) ** 2))

        # Add measurements onto the diagnostic image
        # color blind friendly palette in BGR: (255, 0, 255) = magenta; (255, 0, 0) = blue
        # Draw convex hull
        cv2.drawContours(plt_img, [hull], -1, (255, 0, 255), 5)
        # Draw perimeter outline
        cv2.drawContours(plt_img, cnt, -1, (255, 0, 0), 5)
        # Draw width
        cv2.line(plt_img, (x, y), (x + width, y), (255, 0, 255), 5)
        # Draw height
        cv2.line(plt_img, (int(cmx), y), (int(cmx), y + height), (255, 0, 255), 5)
        # Draw centroid
        cv2.circle(plt_img, (int(cmx), int(cmy)), 10, (255, 0, 255), 5)

    # Store outputs
    outputs.add_metadata(term="image_height", datatype=int, value=np.shape(img)[0])
    outputs.add_metadata(term="image_width", datatype=int, value=np.shape(img)[1])
    # the error you are looking for is below
    outputs.add_observation(sample=label, variable='area', trait='area',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=area, label="pixels")
    # the error you are looking for is above
    outputs.add_observation(sample=label, variable='convex_hull_area', trait='convex hull area',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=hull_area, label="pixels")
    outputs.add_observation(sample=label, variable='solidity', trait='solidity',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=float,
                            value=solidity, label='none')
    outputs.add_observation(sample=label, variable='perimeter', trait='perimeter',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=perimeter, label="pixels")
    outputs.add_observation(sample=label, variable='total_edge_length', trait='total length of object edges',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=total_edge_length, label="pixels")
    outputs.add_observation(sample=label, variable='width', trait='width',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=width, label="pixels")
    outputs.add_observation(sample=label, variable='height', trait='height',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=height, label="pixels")
    outputs.add_observation(sample=label, variable='center_of_mass', trait='center of mass',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=tuple,
                            value=(cmx, cmy), label=("x", "y"))
    outputs.add_observation(sample=label, variable='convex_hull_vertices', trait='convex hull vertices',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=int,
                            value=hull_vertices, label='none')
    outputs.add_observation(sample=label, variable='object_in_frame', trait='object in frame',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=bool,
                            value=in_bounds, label='none')
    outputs.add_observation(sample=label, variable='ellipse_center', trait='ellipse center',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=tuple,
                            value=(ellipse_center[0], ellipse_center[1]), label=("x", "y"))
    outputs.add_observation(sample=label, variable='ellipse_major_axis', trait='ellipse major axis length',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=ellipse_major_axis, label="pixels")
    outputs.add_observation(sample=label, variable='ellipse_minor_axis', trait='ellipse minor axis length',
                            method='plantcv.plantcv.analyze.size', scale="pixels", datatype=int,
                            value=ellipse_minor_axis, label="pixels")
    outputs.add_observation(sample=label, variable='ellipse_angle', trait='ellipse major axis angle',
                            method='plantcv.plantcv.analyze.size', scale='degrees', datatype=float,
                            value=float(ellipse_angle), label='degrees')
    outputs.add_observation(sample=label, variable='ellipse_eccentricity', trait='ellipse eccentricity',
                            method='plantcv.plantcv.analyze.size', scale='none', datatype=float,
                            value=float(ellipse_eccentricity), label='none')
    return plt_img, outputs


def _object_composition(contours, hierarchy):
    """
    Groups objects into a single object, usually done after object filtering.

    Inputs:
    contours  = Contour tuple
    hierarchy = Contour hierarchy NumPy array

    Returns:
    group    = grouped contours list

    :param contours: tuple
    :param hierarchy: numpy.ndarray
    :return group: numpy.ndarray
    """
    stack = np.zeros((len(contours), 1))

    for c, _ in enumerate(contours):
        if hierarchy[0][c][2] == -1 and hierarchy[0][c][3] > -1:
            stack[c] = 0
        else:
            stack[c] = 1

    ids = np.where(stack == 1)[0]
    group = np.array([], dtype=np.int32)
    if len(ids) > 0:
        contour_list = [contours[i] for i in ids]
        group = np.vstack(contour_list)

    return group
