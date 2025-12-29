import pandas as pd
import numpy as np

def compute_momentum(
    df: pd.DataFrame,
    window: int = 5
) -> pd.DataFrame:
    """
    Compute team momentum as slope of recent points.
    """

    df = df.copy()
    df = df.sort_values(['team', 'date'])

    df['momentum'] = (
        df
        .groupby('team')['points']
        .transform(
            lambda x: x.rolling(window=window, min_periods=2)
                      .apply(_linear_slope, raw=True)
        )
    )

    df['momentum'] = df['momentum'].fillna(0)

    return df

def _linear_slope(values: np.ndarray) -> float:
    """
    Compute slope of a linear regression over equally spaced points.
    """

    if len(values) < 2:
        return 0.0

    x = np.arange(len(values))
    y = values

    slope = np.polyfit(x, y, 1)[0]
    return slope
