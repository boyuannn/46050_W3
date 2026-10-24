# csv_labeler/compute_modules.py
from csv_labeler import functions, filter as filt, compute

def tau_summary(raw_dir):
    """Load, filter and summarise CSF tau for each group in one step."""
    df = functions.load_all(raw_dir)
    df = filt.keep_columns(df, ["PTID", "label", "TAU_FINAL"])
    df = filt.drop_shared_ids(df)
    return compute.group_summary(df, "TAU_FINAL")