import pandas as pd
import numpy as np
from src.features.form import compute_points, compute_form
from src.features.momentum import compute_momentum

def build_dataset (df: pd.DataFrame) -> pd.DataFrame:
    '''
    Build dataset for model training.
    '''

    df = df.copy()

    # Example feature engineering
    df['win'] = (df['goals_for'] > df['goals_against']).astype(int)
    
    dataset = df[['team', 'date', 'momentum', 'win']]


    return dataset
def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build pre-match features for modeling.
    """

    df = df.copy()

    df = compute_points(df)
    df = compute_form(df, window=5)
    df = compute_momentum(df, window=5)

    return df

def build_prematch_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build pre-match dataset with home and away features.
    """

    df = df.copy()

    home = (
        df[df['is_home'] == 1]
        .rename(columns={
            'team': 'home_team',
            'form': 'home_form',
            'momentum': 'home_momentum'
        })
    )

    away = (
        df[df['is_home'] == 0]
        .rename(columns={
            'team': 'away_team',
            'form': 'away_form',
            'momentum': 'away_momentum'
        })
    )

    prematch = (
        home
        .merge(
            away,
            on=['match_id', 'date'],
            how='inner',
            suffixes=('', '_away')
        )
    )

    cols = [
        'match_id',
        'date',
        'home_team',
        'away_team',
        'home_form',
        'away_form',
        'home_momentum',
        'away_momentum'
    ]

    return prematch[cols]
