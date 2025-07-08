## This file builds ML pipeline to predict game outcomes and goal counts
## using Random Forest for classification and regression

import pandas as pd
import glob
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load all match CSVs
csv_files = glob.glob('./data/*.csv')
dfs = [pd.read_csv(f) for f in csv_files]
matches = pd.concat(dfs, ignore_index=True)
print(f"Shape after loading match CSVs: {matches.shape}")


# Step 2: Load the aggregated team stats
team_stats = pd.read_csv('./data/aggregated_team_stats.csv', index_col=0)
print(f"Shape of team_stats: {team_stats.shape}")
print("Columns in team_stats:", team_stats.columns.tolist())

# Strip whitespace from team names in both dataframes
matches['HomeTeam'] = matches['HomeTeam'].str.strip()
matches['AwayTeam'] = matches['AwayTeam'].str.strip()
team_stats.index = team_stats.index.str.strip()


# Create copies of team_stats for home and away merges
# And rename columns to be distinct for the match context

# For Home Team stats:
team_stats_for_home_merge = team_stats.copy()

# Rename existing columns in team_stats to distinguish them as 'HomeTeam's stats
# We'll prepend 'HomeTeam_' to each original stat name
team_stats_for_home_merge.columns = ['HomeTeam_' + col for col in team_stats_for_home_merge.columns]

matches = matches.merge(
    team_stats_for_home_merge,
    left_on='HomeTeam',
    right_index=True,
    how='left'
)

# For Away Team stats:
team_stats_for_away_merge = team_stats.copy()
# Rename existing columns in team_stats to distinguish them as 'AwayTeam's stats
# We'll prepend 'AwayTeam_' to each original stat name
team_stats_for_away_merge.columns = ['AwayTeam_' + col for col in team_stats_for_away_merge.columns]

print("Merging Away Team stats...")
matches = matches.merge(
    team_stats_for_away_merge,
    left_on='AwayTeam',
    right_index=True,
    how='left'
)

# Step 5: Prepare features — select relevant columns
# Now, update your feature_cols to reflect the new column names
feature_cols = [
    # Home team stats (prefixed with 'HomeTeam_')
    'HomeTeam_avg_goals_for_home', 'HomeTeam_avg_goals_against_home', 'HomeTeam_avg_shots_home',
    'HomeTeam_avg_shots_on_target_home', 'HomeTeam_avg_corners_home', 'HomeTeam_avg_fouls_home',
    'HomeTeam_avg_yellows_home', 'HomeTeam_avg_reds_home',
    'HomeTeam_avg_goals_for_away', 'HomeTeam_avg_goals_against_away', 'HomeTeam_avg_shots_away',
    'HomeTeam_avg_shots_on_target_away', 'HomeTeam_avg_corners_away', 'HomeTeam_avg_fouls_away',
    'HomeTeam_avg_yellows_away', 'HomeTeam_avg_reds_away',
    
    # Away team stats (prefixed with 'AwayTeam_')
    'AwayTeam_avg_goals_for_home', 'AwayTeam_avg_goals_against_home', 'AwayTeam_avg_shots_home',
    'AwayTeam_avg_shots_on_target_home', 'AwayTeam_avg_corners_home', 'AwayTeam_avg_fouls_home',
    'AwayTeam_avg_yellows_home', 'AwayTeam_avg_reds_home',
    'AwayTeam_avg_goals_for_away', 'AwayTeam_avg_goals_against_away', 'AwayTeam_avg_shots_away',
    'AwayTeam_avg_shots_on_target_away', 'AwayTeam_avg_corners_away', 'AwayTeam_avg_fouls_away',
    'AwayTeam_avg_yellows_away', 'AwayTeam_avg_reds_away',
]

matches = matches.dropna(subset=feature_cols + ['FTR'])

if matches.shape[0] == 0:
    print("Error: No data left after dropping NaNs. This indicates an issue with merging or missing data.")
    print("Please check the team names in your match data and team_stats data for consistency (case, leading/trailing spaces).")
    
    # More detailed check: which teams are missing stats?
    # This checks for NaNs specifically in the *newly merged* columns
    missing_home_stats_teams = matches[matches['HomeTeam_avg_goals_for_home'].isnull()]['HomeTeam'].unique()
    missing_away_stats_teams = matches[matches['AwayTeam_avg_goals_for_home'].isnull()]['AwayTeam'].unique()
    
    if len(missing_home_stats_teams) > 0:
        print(f"Home teams with missing stats: {missing_home_stats_teams}")
    if len(missing_away_stats_teams) > 0:
        print(f"Away teams with missing stats: {missing_away_stats_teams}")
    
    print("Team names in team_stats index (for comparison):", team_stats.index.tolist())
    exit()

X = matches[feature_cols]
y = matches['FTR']  # Target: 'H', 'D', 'A'
y_home_goals = matches['FTHG']  # Full Time Home Goals
y_away_goals = matches['FTAG']  # Full Time Away Goals
# Encode target labels (H=Home Win, D=1, A=2)
label_map = {'H': 0, 'D': 1, 'A': 2}
y = y.map(label_map)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Class distribution:", y.value_counts())

# Ensure there's enough data to split
if X.shape[0] < 2:
    print("Error: Not enough samples to perform train_test_split. Need at least 2 samples.")
    exit()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# Step 7: Train the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Train the Random Forest Regressor
reg_home = RandomForestRegressor(n_estimators=100, random_state=42)
reg_home.fit(X, y_home_goals)
joblib.dump(reg_home, './model/home_goals_rf.joblib')
print("Home goals regression model saved to ./model/home_goals_rf.joblib")

reg_away = RandomForestRegressor(n_estimators=100, random_state=42)
reg_away.fit(X, y_away_goals)
joblib.dump(reg_away, './model/away_goals_rf.joblib')
print("Away goals regression model saved to ./model/away_goals_rf.joblib")


# Step 8: Evaluate the model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['Home Win', 'Draw', 'Away Win']))

# Step 9: Save the model for later use
joblib.dump(clf, './model/match_predictor_rf.joblib')
print("Model saved to ./model/match_predictor_rf.joblib")