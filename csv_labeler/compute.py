"""Compute step: summary numbers for each diagnosis group."""

GROUP_NAMES = {0: "CN", 1: "MCI", 2: "AD"}


def group_summary(df, column):
    """Mean, standard deviation and count of one column for each group.

    :param df: filtered table with a "label" column
    :param column: column to summarise, e.g. "TAU_FINAL"
    :return: a table with one row per group (CN, MCI, AD)
    """
    summary = df.groupby("label")[column].agg(["mean", "std", "count"])
    summary.index = summary.index.map(GROUP_NAMES)
    return summary.round(1)
