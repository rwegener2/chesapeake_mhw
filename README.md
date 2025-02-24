chesapeake_mhw
==============================

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
