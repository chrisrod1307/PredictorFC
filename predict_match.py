## This file uses previously trained ML models to predict who will win match and predicted scoreline

import pandas as pd
import joblib

# Load model
model = joblib.load('./model/match_predictor_rf.joblib')
model_home_goals = joblib.load('./model/home_goals_rf.joblib')
model_away_goals = joblib.load('./model/away_goals_rf.joblib')

# Load team stats
team_stats = pd.read_csv('./data/aggregated_team_stats.csv', index_col=0)
team_stats.index = team_stats.index.str.strip()

# Get user input for teams
print(f"Teams:" + team_stats.index)
home_team = input("Enter home team: ").strip()
away_team = input("Enter away team: ").strip()

# Check if teams exist in stats
if home_team not in team_stats.index:
    print(f"Error: Home team '{home_team}' not found in team stats.")
    exit()
if away_team not in team_stats.index:
    print(f"Error: Away team '{away_team}' not found in team stats.")
    exit()

# Extract stats
home_stats = team_stats.loc[home_team]
away_stats = team_stats.loc[away_team]

# Build input feature dict
features = {
    # Home team stats
    'HomeTeam_avg_goals_for_home': home_stats['avg_goals_for_home'],
    'HomeTeam_avg_goals_against_home': home_stats['avg_goals_against_home'],
    'HomeTeam_avg_shots_home': home_stats['avg_shots_home'],
    'HomeTeam_avg_shots_on_target_home': home_stats['avg_shots_on_target_home'],
    'HomeTeam_avg_corners_home': home_stats['avg_corners_home'],
    'HomeTeam_avg_fouls_home': home_stats['avg_fouls_home'],
    'HomeTeam_avg_yellows_home': home_stats['avg_yellows_home'],
    'HomeTeam_avg_reds_home': home_stats['avg_reds_home'],
    'HomeTeam_avg_goals_for_away': home_stats['avg_goals_for_away'],
    'HomeTeam_avg_goals_against_away': home_stats['avg_goals_against_away'],
    'HomeTeam_avg_shots_away': home_stats['avg_shots_away'],
    'HomeTeam_avg_shots_on_target_away': home_stats['avg_shots_on_target_away'],
    'HomeTeam_avg_corners_away': home_stats['avg_corners_away'],
    'HomeTeam_avg_fouls_away': home_stats['avg_fouls_away'],
    'HomeTeam_avg_yellows_away': home_stats['avg_yellows_away'],
    'HomeTeam_avg_reds_away': home_stats['avg_reds_away'],

    # Away team stats
    'AwayTeam_avg_goals_for_home': away_stats['avg_goals_for_home'],
    'AwayTeam_avg_goals_against_home': away_stats['avg_goals_against_home'],
    'AwayTeam_avg_shots_home': away_stats['avg_shots_home'],
    'AwayTeam_avg_shots_on_target_home': away_stats['avg_shots_on_target_home'],
    'AwayTeam_avg_corners_home': away_stats['avg_corners_home'],
    'AwayTeam_avg_fouls_home': away_stats['avg_fouls_home'],
    'AwayTeam_avg_yellows_home': away_stats['avg_yellows_home'],
    'AwayTeam_avg_reds_home': away_stats['avg_reds_home'],
    'AwayTeam_avg_goals_for_away': away_stats['avg_goals_for_away'],
    'AwayTeam_avg_goals_against_away': away_stats['avg_goals_against_away'],
    'AwayTeam_avg_shots_away': away_stats['avg_shots_away'],
    'AwayTeam_avg_shots_on_target_away': away_stats['avg_shots_on_target_away'],
    'AwayTeam_avg_corners_away': away_stats['avg_corners_away'],
    'AwayTeam_avg_fouls_away': away_stats['avg_fouls_away'],
    'AwayTeam_avg_yellows_away': away_stats['avg_yellows_away'],
    'AwayTeam_avg_reds_away': away_stats['avg_reds_away'],
}

# Create DataFrame for model input
input_df = pd.DataFrame([features])

# Predict result (H/D/A)
result_pred = model.predict(input_df)[0]
label_map = {0: 'Home Win', 1: 'Draw', 2: 'Away Win'}

# Predict score
pred_home_goals = model_home_goals.predict(input_df)[0]
pred_away_goals = model_away_goals.predict(input_df)[0]

# Round and convert to int
home_goals_pred = int(round(pred_home_goals))
away_goals_pred = int(round(pred_away_goals))

# Determine match result from predicted scores
if home_goals_pred > away_goals_pred:
    result_str = f"{home_team} wins"
elif home_goals_pred < away_goals_pred:
    result_str = f"{away_team} wins"
else:
    result_str = "Draw"

# Display final prediction
print(f"\nPrediction for match: {home_team} vs {away_team}")
print(f"Predicted Score: {home_team} {home_goals_pred} - {away_goals_pred} {away_team}")
print(f"Match Result Prediction: {result_str}")
