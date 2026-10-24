"""Report step: plot one measure for each diagnosis group."""
import matplotlib.pyplot as plt

from csv_labeler.compute import GROUP_NAMES


def plot_groups(df, column, ylabel=None, title=None):
    """Box plot of one column for each diagnosis group.

    :param df: filtered table with a "label" column
    :param column: column to plot, e.g. "TAU_FINAL"
    :param ylabel: y-axis label (default: the column name)
    :param title: plot title (default: none)
    :return: (fig, ax) so the plot can be saved or changed later
    """
    labels = sorted(df["label"].unique())
    groups = [df.loc[df["label"] == lab, column].dropna() for lab in labels]

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.boxplot(groups)
    ax.set_xticks(range(1, len(labels) + 1), [GROUP_NAMES[lab] for lab in labels])
    ax.set_ylabel(ylabel or column)
    if title:
        ax.set_title(title)
    return fig, ax
