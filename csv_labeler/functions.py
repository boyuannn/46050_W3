import pandas as pd

def load_and_label(path, label):
    """Read in a CSV file, delete the unnecessary row numbers and columns, and add a column of    diagnostic labels

    path:  CSV path
    label: CN=0, MCI=1, AD=2
    """
    df = pd.read_csv(path)
    df = df.drop(columns=["Unnamed: 0"])
    df["label"] = label
    return df

def load_all(raw_dir):
    """Load the CN, MCI and AD files and combine them into one table.

    :param raw_dir: folder with CN.new.csv, MCI.new.csv and AD.new.csv
    :return: one table with a label column (CN=0, MCI=1, AD=2)
    """
    files = {"CN.new.csv": 0, "MCI.new.csv": 1, "AD.new.csv": 2}
    tables = [load_and_label(raw_dir / name, label) for name, label in files.items()]
    return pd.concat(tables, ignore_index=True)
