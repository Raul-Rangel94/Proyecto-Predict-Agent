import pandas as pd

def build_team_view(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform match-level data into team-level perspective.
    """

    home = pd.DataFrame({
        "match_id": df["match_id"],
        "date": df["date"],
        "team": df["home_team"],
        "goals_for": df["home_goals"],
        "goals_against": df["away_goals"],
        "is_home": 1
    })

    away = pd.DataFrame({
        "match_id": df["match_id"],
        "date": df["date"],
        "team": df["away_team"],
        "goals_for": df["away_goals"],
        "goals_against": df["home_goals"],
        "is_home": 0
    })

    team_df = pd.concat([home, away], ignore_index=True)

    team_df = team_df.sort_values(["team", "date"]).reset_index(drop=True)


    return team_df
