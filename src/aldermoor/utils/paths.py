"""Project paths and safe file loading for the Aldermoor project.

PROJECT_ROOT is found from this file's location, so it is correct
wherever the code is run from.
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