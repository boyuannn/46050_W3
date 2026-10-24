# README #

### What is this repository for? ###

* ADNI data pipeline: does CSF tau differ between CN, MCI and AD?
* Load → Filter → Compute → Statistics → Report, one module for each step
  in the `csv_labeler` package.

### How do I get set up? ###

* clone repo
* `conda env create -f environment.yml` create a new environment from the .yml file
* `pip install .` in that environment

### Data ###

* You will need the ADNI clinical files: `CN.new.csv`, `MCI.new.csv`, `AD.new.csv`.
  ADNI data cannot be shared, so it is not in this repo.
* Put them in `~/Data/ADNI_project/raw/`. The path is set in `csv_labeler/config.py`.

### How to run ###

* Open `notebook/w4.ipynb` and Run All.