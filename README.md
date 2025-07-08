# PredictorFC

PredictorFC is a machine learning-based web application that predicts Premier League soccer match outcomes and scores using data from the 2020-2021 -> 2024-2025 Premier League Season. It combines a React frontend with a Django backend to deliver real-time predictions based on team statistics.

---

## Features

- **Match Result Prediction:** Predicts whether the home team will win, draw, or lose.
- **Score Prediction:** Estimates the number of goals each team is likely to score.
- **Data-Driven:** Uses historical match data and aggregated team stats for accurate modeling.
- **Interactive UI:** Users select home and away teams to get instant predictions.
- **Trained Models:** Utilizes Random Forest classifiers and regressors for predictions.

---

## Technologies Used

- **Frontend:** React, JavaScript, Tailwind CSS, Headless UI
- **Backend:** Python, scikit-learn, pandas
- **Machine Learning:** Random Forest Classifier and Regressor
- **Version Control:** Git & GitHub

---

## Getting Started

### Backend Setup

1. Run model training script (optional, if you want to retrain):

    ```bash
    python train_model.py
    ```
    
2. Navigate to the backend folder:

    ```bash
    cd backend_django
    ```

3. Run backend server
   
    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. Navigate to the React app folder:

    ```bash
    cd frontend_react
    ```

2. Install dependencies:

    ```bash
    npm install
    # or
    yarn install
    ```

3. Run the React development server:

    ```bash
    npm start
    # or
    yarn start
    ```

---

## Usage

1. Open the React app in your localhost
2. Select the home and away teams from the dropdown.
3. View predicted match results and scores.

---

## Notes

- Models are saved in the `/model` directory.
- Make sure team names match exactly between datasets and frontend inputs to avoid errors.

---

## Contact

Created by Christian Rodriguez  

Email: rodriguez.christian325@gmail.com

LinkedIn: [https://www.linkedin.com/in/christian-rodriguezucf/]

GitHub: [https://github.com/chrisrod1307](https://github.com/chrisrod1307)

---

Feel free to open issues or submit pull requests!


