chesapeake_mhw
==============================
[![Build Status](https://github.com/rwegener2/chesapeake_mhw/workflows/Tests/badge.svg)](https://github.com/rwegener2/chesapeake_mhw/actions)
[![codecov](https://codecov.io/gh/rwegener2/chesapeake_mhw/branch/main/graph/badge.svg)](https://codecov.io/gh/rwegener2/chesapeake_mhw)
[![License:BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-lightgray.svg?style=flt-square)](https://opensource.org/licenses/BSD-3-Clause)
[![pypi](https://img.shields.io/pypi/v/chesapeake_mhw.svg)](https://pypi.org/project/chesapeake_mhw)
<!-- [![conda-forge](https://img.shields.io/conda/dn/conda-forge/chesapeake_mhw?label=conda-forge)](https://anaconda.org/conda-forge/chesapeake_mhw) -->[![Documentation Status](https://readthedocs.org/projects/chesapeake_mhw/badge/?version=latest)](https://chesapeake_mhw.readthedocs.io/en/latest/?badge=latest)


Code to support the publication

This repository contains code to support the publication ______.

### Environment Setup

To setup this environment use ...

### Reproducing the pipeline

Overview of Steps:

1. Download the datasets: geopolar, nasa mur, Chesepeake Bay program in situ data, either from Zenodo or using the scripts provided. There should then be 3 datasets in the `data/raw` folder.
2. Run the notebooks in the `notebooks` folder. This generates the figures.

### Organization

#### `data` Folder

Folders created to hold data throughout the processing pipeline, from raw data to fully processed data. The folders are empty on github, but the data can be processed using:
1. running the Python files which contain code to search, subset, and download the data. These are located in the `data_download` folder
2. Download each of the 3 datasets individually from Zenodo and move them into the `raw` data folder.

#### `figures` Folder

Contains the final figures, as generated in the data analysis notebooks

### `notebooks` Folder

Jupyter notebooks written in Python with instructions for processing the data from the `raw` format through the generation of relevant `figures`.

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
