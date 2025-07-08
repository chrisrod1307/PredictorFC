## This file loads multiple PL csv's and calculates the averages for the aggregated_team_stats file

import pandas as pd
import glob

# 1. Load all CSVs from data folder
csv_files = glob.glob('./Data/PL_*.csv')

dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# 2. Combine all seasons into one DataFrame
all_data = pd.concat(dfs, ignore_index=True)

# 3. Calculate stats per team, split by Home and Away
home_stats = all_data.groupby('HomeTeam').agg({
    'FTHG': 'mean',   # Avg goals scored at home
    'FTAG': 'mean',   # Avg goals conceded at home
    'HS': 'mean',     # Home shots
    'HST': 'mean',    # Home shots on target
    'HC': 'mean',     # Home corners
    'HF': 'mean',     # Home fouls
    'HY': 'mean',     # Home yellow cards
    'HR': 'mean',     # Home red cards
}).rename(columns={
    'FTHG': 'avg_goals_for_home',
    'FTAG': 'avg_goals_against_home',
    'HS': 'avg_shots_home',
    'HST': 'avg_shots_on_target_home',
    'HC': 'avg_corners_home',
    'HF': 'avg_fouls_home',
    'HY': 'avg_yellows_home',
    'HR': 'avg_reds_home',
})

away_stats = all_data.groupby('AwayTeam').agg({
    'FTAG': 'mean',   # Avg goals scored away
    'FTHG': 'mean',   # Avg goals conceded away
    'AS': 'mean',     # Away shots
    'AST': 'mean',    # Away shots on target
    'AC': 'mean',     # Away corners
    'AF': 'mean',     # Away fouls
    'AY': 'mean',     # Away yellow cards
    'AR': 'mean',     # Away red cards
}).rename(columns={
    'FTAG': 'avg_goals_for_away',
    'FTHG': 'avg_goals_against_away',
    'AS': 'avg_shots_away',
    'AST': 'avg_shots_on_target_away',
    'AC': 'avg_corners_away',
    'AF': 'avg_fouls_away',
    'AY': 'avg_yellows_away',
    'AR': 'avg_reds_away',
})

# 4. Merge home and away stats into one DataFrame by team
team_stats = pd.merge(home_stats, away_stats, left_index=True, right_index=True)

# 5. Save aggregated team stats CSV
team_stats.to_csv('./data/aggregated_team_stats.csv')
print("Aggregated team stats saved!")