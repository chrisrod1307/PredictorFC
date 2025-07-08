from django.shortcuts import render
import json
import joblib
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load model
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'match_predictor_rf.joblib')
model = joblib.load(MODEL_PATH)

HOME_GOALS_MODEL_PATH = os.path.join(BASE_DIR, 'model', 'home_goals_rf.joblib')
model_home_goals = joblib.load(HOME_GOALS_MODEL_PATH)

AWAY_GOALS_MODEL_PATH = os.path.join(BASE_DIR, 'model', 'away_goals_rf.joblib')
model_away_goals = joblib.load(AWAY_GOALS_MODEL_PATH)

# Load team stats
STATS_PATH = os.path.join(BASE_DIR, 'data', 'aggregated_team_stats.csv')
team_stats = pd.read_csv(STATS_PATH, index_col=0)

# Label mapping for output
label_map = {0: 'Home Win', 1: 'Draw', 2: 'Away Win'}

@csrf_exempt
def predict_match(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            home_team = data['home_team'].strip()
            away_team = data['away_team'].strip()

            # Get team stats
            home_stats = team_stats.loc[home_team].add_prefix('HomeTeam_')
            away_stats = team_stats.loc[away_team].add_prefix('AwayTeam_')

            # Combine stats into one row
            match_features = pd.concat([home_stats, away_stats])[model.feature_names_in_].to_frame().T

            # Predict Result
            prediction = model.predict(match_features)[0]

            # Predict scores
            pred_home_goals = model_home_goals.predict(match_features)[0]
            pred_away_goals = model_away_goals.predict(match_features)[0]

            home_goals_pred = int(round(pred_home_goals))
            away_goals_pred = int(round(pred_away_goals))

             # Build result string based on score prediction (can differ from classification)
            if home_goals_pred > away_goals_pred:
                result_str = f"{home_team} wins"
            elif home_goals_pred < away_goals_pred:
                result_str = f"{away_team} wins"
            else:
                result_str = "Draw"

            return JsonResponse({
                'home_team': home_team,
                'away_team': away_team,
                'home_score': home_goals_pred,
                'away_score': away_goals_pred,
                'prediction': result_str
            })

        except KeyError as e:
            return JsonResponse({'error': f'Missing or incorrect team name: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
