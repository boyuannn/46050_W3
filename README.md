# W3

`load_and_label(path, label)` reads one CSV file, removes the unused
row-number column, and adds a diagnosis label column (CN=0, MCI=1, AD=2).

## How to run the notebook
```
conda env create -f environment.yml
conda activate W3
jupyter lab W3.ipynb
```

## Install as a Python package
The function is also available as the `csv_labeler` package. With the `W3`
environment active, run this from the repo folder:
```
pip install -e .
```

## Usage
```python
from csv_labeler.functions import load_and_label

df = load_and_label("data/CN.csv", 0)
```