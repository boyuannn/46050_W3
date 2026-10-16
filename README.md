# W3

`load_and_label(path, label)` reads one CSV file, removes the unused
row-number column, and adds a diagnosis label column (CN=0, MCI=1, AD=2).

## How to run
conda env create -f environment.yml
conda activate label-demo
jupyter lab test.ipynb# 46050_W3
