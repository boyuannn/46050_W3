"""Paths to the data folders. Change DATA_DIR if your data lives somewhere else."""
from pathlib import Path

DATA_DIR = Path.home() / "Data" / "ADNI_project"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
