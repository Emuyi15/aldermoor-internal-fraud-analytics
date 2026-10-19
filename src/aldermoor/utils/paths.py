"""
A module that loads files from data directory and raise a clear FileNotFoundError
"""

# import path and pandas
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data"

def load_csv(path: Path) -> pd.DataFrame:
    """Read a CSV file, raising a clear FileNotFoundErorr
    if it does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Expected data file not found: {path}")
    return pd.read_csv(path)