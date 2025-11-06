# Contributing to PlantCV

This repository is a place for you to learn to contribute to PlantCV in one of our guided new contributor workshops. For full documentation or asynchronous learning about contributing to PlantCV please see the [contribution docs](http://plantcv.readthedocs.io/en/latest/CONTRIBUTING/).

## Getting started

To get started you will need an environment with at least `numpy`, `cv2`, and `...` python libraries installed. If you are looking to contribute to PlantCV then you may already have a conda environment set up for PlantCV and that would work great for this as well.

### Installing littlecv

Clone this repository, `cd` to the base of this repo, and run `pip install -e .` Note that this is basically the same way you will set up your editable `PlantCV` installation for when you are contributing to the codebase.

## The task

In this repository there is a small Python library called `littleCV`, these are just a handful of `PlantCV` functions with some of the more complicated features removed.

There is also an iPython notebook running a simple workflow using `littleCV`. In the course of running that notebook there will be bugs in those functions that you'll need to fix. The point of this task is not to do complex troubleshooting but just to familiarize with making edits and contributing to a version controlled codebase like `PlantCV`.

The final piece of the `workflow.ipynb` checks the area phenotype, when that check returns `True` you have made the required edit in the `littlecv` codebase and you can send your edits to github. You should not be editing steps in the `workflow.ipynb` file to try to make that last statement return `True`, the only changes you need to make are in the codebase.


### The Functions

`littlecv` only has 6 exposed functions, they are:

* `readimage`: Reads an image into a numpy.ndarray. Simplified from `plantcv.plantcv.read_image`
* `rgb2gray_lab`: Converts an RGB image to grayscale with either L, A, or B channel. Simplified from `plantcv.plantcv.rgb2gray_lab`.
* `binary`: Applies a binary threshold. Simplified from `plantcv.plantcv.threshold.binary`.
* `fill`: Filters small objects. Simplified from `plantcv.plantcv.fill`.
* `size`: Calculates single value phenotypes given a mask and image. Simplified from `plantcv.analyze.size`
* `plot_image`: Plots an image. Simplified from `plantcv.plantcv.plot_image`.

There is also a minimal `Outputs` class called by `size` to store results which is based on the `plantcv.plantcv.Outputs` class.
