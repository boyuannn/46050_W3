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