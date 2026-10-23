"""Statistics step: test whether the diagnosis groups differ."""
from scipy import stats


def compare_groups(df, column):
    """Kruskal-Wallis test: does one column differ between the groups?

    :param df: filtered table with a "label" column
    :param column: column to test, e.g. "TAU_FINAL"
    :return: (H statistic, p value)
    """
    groups = [g[column].dropna() for _, g in df.groupby("label")]
    result = stats.kruskal(*groups)
    return result.statistic, result.pvalue
