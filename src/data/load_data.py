import pandas as pd
from pathlib import Path

REQUIRED_COLUMNS = ["match_id","home_team", "away_team", "date",
                     "result"]

def load_matches(file_path: str) -> pd.DataFrame:
    """
    Load Liga MX matches from a CSV file.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame with match data.
    """
    
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path} .")
    
    df = pd.read_csv(file_path)
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df
