"""Filter step: keep only the rows and columns needed for the analysis."""


def keep_columns(df, columns):
    """Keep only the listed columns.

    :param df: combined table
    :param columns: list of column names to keep
    :return: a new table with only those columns
    """
    return df[columns].copy()


def drop_shared_ids(df, id_col="PTID"):
    """Remove subjects who appear in more than one diagnosis group.

    :param df: combined table with a "label" column
    :param id_col: name of the subject ID column
    :return: a table where every subject has exactly one label
    """
    n_labels = df.groupby(id_col)["label"].nunique()
    shared = n_labels[n_labels > 1].index
    return df[~df[id_col].isin(shared)].reset_index(drop=True)
