# Contributing to PlantCV

This repository is a place for you to learn to contribute to PlantCV in one of our guided new contributor workshops. For full documentation or asynchronous learning about contributing to PlantCV please see the [contribution docs](http://plantcv.readthedocs.io/en/latest/CONTRIBUTING/).

## Getting started

To get started you will need an environment with at least `numpy`, `cv2`, `matplotlib`, `pandas`, `python-dateutil`, and `skikit-image` Python libraries installed. We recommend installing `PlantCV` in editable mode if you have not already done so as that will be best for contributing and will install everything you need for this activity. If you are looking to contribute to PlantCV then you may already have a conda environment set up for `PlantCV` and that would work for this workshop as well, whether `PlantCV` is editable or not in that installation.

### Installing littlecv

* First, Clone this repository (`git clone https://github.com/danforthcenter/contributing_tutorial.git`). Throughout this readme we include git CLI commands but [Github Desktop](https://github.com/apps/desktop), [Git Kraken](https://www.gitkraken.com/), or Git through VSCode/other IDEs are all friendlier options and worth learning to use.
* Next, `cd` to the cloned repo (`cd contributing_tutorial`)
* Finally, with your `PlantCV` or equivalent environment active, install `littlecv` by running `pip install -e .`.

Now you will have an editable version of `littlecv` installed locally. You can check your installation by running this command, which should tell you that you'll be an author soon:

```
python -c "from littlecv import littlecv as lcv; print(lcv.__author__)"
```

## The task

In this repository there is a small Python library called `littleCV`, these are just a handful of `PlantCV` functions with some of the more complicated features removed.

There is also an iPython notebook running a simple workflow using `littleCV`. In the course of running that notebook there will be bugs in those functions that you'll need to fix. The point of this task is not to do complex troubleshooting but just to familiarize with making edits and contributing to a version controlled codebase like `PlantCV`.

The final piece of the `workflow.ipynb` checks the area phenotype, when that check returns `True` you have made the required edit in the `littlecv` codebase and you can send your edits to github. You should not be editing steps in the `workflow.ipynb` file to try to make that last statement return `True`, the only changes you need to make are in the codebase. If you prefer to work outside of jupyter notebooks you can also make edits to the `littlecv` codebase and run the tests for the package with the `py.test --cov littlecv` in the `contributing_tutorial` directory which will run the test in the `contributing_tutorial/tests` directory which makes the same assertion as at the end of the jupyter notebook. Once you are contributing to `PlantCV` you should familiarize with troubleshooting based on reports from `py.test`.


#### Steps

* 1: Open a branch with your name (`git checkout -b first_last`).
* 2: Check current behavior either in jupyter (run `jupyter-lab` and use GUI) or with the tests (run `py.test --cov littlecv --cov-report="term-missing"`)
* 3: Edit `littlecv` code.
* 4: Restart Jupyter Kernel and run all cells again or rerun tests. Make edits and test them until tests pass.
* 5: Commit your changes (`git commit -m "your commit message here"`). This is like saving the files on your branch. How often you do this and how granular commits are is mostly up to you.
* 6: Push your changes to github (`git push origin main`). This syncs the changes you've committed to github so that other people could pull them and use them locally.
* 7: Open a Pull Request. These are a feature of Github, not of Git itself, so we'll have to do this online or through a software like Github Desktop. Go to `https://github.com/danforthcenter/contributing_tutorial/tree/YOUR_BRANCH_NAME` or to [`https://github.com/danforthcenter/contributing_tutorial`](https://github.com/danforthcenter/contributing_tutorial) and use the branch dropdown menu to select your branch. On your branch there should be a green `Compare and pull request` button, click that and fill out the template. There is a sidebar of options for labels, assignees, reviewers, etc. In `PlantCV` you'll; use those to describe the purpose of your PR at a very high level, mark it for a certain version milestone or request certain reviewers based on who has domain expertise or last edited those files. Once you are done with the description click `create pull request`. Once the pull request is created the automated checks will run, if those pass then you are done!

### The Functions

`littlecv` only has 6 exposed functions, they are:

* `readimage`: Reads an image into a numpy.ndarray. Simplified from `plantcv.plantcv.read_image`
* `rgb2gray_lab`: Converts an RGB image to grayscale with either L, A, or B channel. Simplified from `plantcv.plantcv.rgb2gray_lab`.
* `binary`: Applies a binary threshold. Simplified from `plantcv.plantcv.threshold.binary`.
* `fill`: Filters small objects. Simplified from `plantcv.plantcv.fill`.
* `size`: Calculates single value phenotypes given a mask and image. Simplified from `plantcv.analyze.size`
* `plot_image`: Plots an image. Simplified from `plantcv.plantcv.plot_image`.

There is also a minimal `Outputs` class called by `size` to store results which is based on the `plantcv.plantcv.Outputs` class.
