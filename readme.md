# Contributing to PlantCV

This repository is a place for you to learn to contribute to PlantCV in one of our guided new contributor workshops. For full documentation or asynchronous learning about contributing to PlantCV please see the [contribution docs](http://plantcv.readthedocs.io/en/latest/CONTRIBUTING/).

## Getting started

To get started you will need an environment with at least `numpy`, `cv2`, and `...` python libraries installed. If you are looking to contribute to PlantCV then you may already have a conda environment set up for PlantCV and that would work great for this as well.

### Installing littlecv

Clone this repository, `cd` to the base of this repo, run `pip install -e .` Note that this is basically the same way you will set up your editable `PlantCV` installation for when you are contributing to the codebase.

## The task

In this repository there is a small Python library called `littleCV`, these are just a handful of `PlantCV` functions with some extra complications removed.
There are a few bugs in those functions that you'll need to fix.

### The Functions

roughly
* littlecv.read_image
* littlecv.threshold
* littlecv.plot_image
* littlecv.analyze_size
* littlecv.print_image
