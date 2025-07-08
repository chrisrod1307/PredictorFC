import { useState } from 'react';
import TeamSelector from './components/TeamSelector';

import aggregatedTeamStats from './data/aggregatedTeamStats';
const PredictForm = () => {
    const [homeTeam, setHomeTeamState] = useState(null);
    const [awayTeam, setAwayTeamState] = useState(null);
    const [homeScore, setHomeScore] = useState('');
    const [awayScore, setAwayScore] = useState('');
    const [result, setResult] = useState(null);

    const setHomeTeam = (team) => {
        setHomeTeamState(team);
        setResult(null);
        setHomeScore('');
        setAwayScore('');
    };

    const setAwayTeam = (team) => {
        setAwayTeamState(team);
        setResult(null);
        setHomeScore('');
        setAwayScore('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!homeTeam || !awayTeam) return;  // safeguard

        const response = await fetch('http://localhost:8000/api/predict/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                home_team: homeTeam.name,
                away_team: awayTeam.name,
            }),
        });

        const data = await response.json();
        setResult(data.prediction);
        setHomeScore(data.home_score);
        setAwayScore(data.away_score);
    };

    return (
        <div className="flex pt-12 justify-center items-center min-h-[calc(100vh-160px)] px-4 bg-cover bg-center">
            <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-3xl">
                <h2 className="text-2xl font-semibold text-center mb-6 text-gray-800">
                    Match Predictor
                </h2>

                <form onSubmit={handleSubmit} className="space-y-6">
                    <div>
                        <label className="block font-medium mb-1">Home Team:</label>
                        <TeamSelector selectedTeam={homeTeam} setSelectedTeam={setHomeTeam} />
                    </div>

                    <div>
                        <label className="block font-medium mb-1">Away Team:</label>
                        <TeamSelector selectedTeam={awayTeam} setSelectedTeam={setAwayTeam} />
                    </div>

                    <button
                        type="submit"
                        disabled={!homeTeam || !awayTeam}
                        className={`
              w-full
              px-4 py-2
              rounded-md
              text-white font-semibold
              transition
              focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500
              ${!homeTeam || !awayTeam
                                ? 'bg-gray-400 cursor-not-allowed'
                                : 'bg-blue-600 hover:bg-blue-700'}
            `}
                    >
                        Predict
                    </button>
                </form>

                {result && (
                    <div className="mt-8 flex items-center justify-center space-x-10">
                        {/* Home Team */}
                        <div className="flex flex-col items-center">
                            <img src={homeTeam.logo} alt={homeTeam.name} className="w-16 h-16 object-contain" />
                            <span className="font-semibold mt-1">{homeTeam.name}</span>
                            <span className="text-2xl font-bold mt-2">{homeScore}</span>
                        </div>

                        <div className="text-lg font-semibold">vs</div>

                        {/* Away Team */}
                        <div className="flex flex-col items-center">
                            <img src={awayTeam.logo} alt={awayTeam.name} className="w-16 h-16 object-contain" />
                            <span className="font-semibold mt-1">{awayTeam.name}</span>
                            <span className="text-2xl font-bold mt-2">{awayScore}</span>
                        </div>
                    </div>
                )}

                {/* Stats Comparison */}
                {result && homeTeam && awayTeam && (() => {
                    const homeStats = aggregatedTeamStats.find(t => t.HomeTeam === homeTeam.name);
                    const awayStats = aggregatedTeamStats.find(t => t.HomeTeam === awayTeam.name);
                    if (!homeStats || !awayStats) return null;

                    return (
                        <div className="mt-10 grid grid-cols-2 gap-8 text-sm bg-white bg-opacity-80 p-6 rounded-lg shadow">
                            {/* Home Team Stats */}
                            <div>
                                <h3 className="text-lg font-semibold text-center mb-2">{homeTeam.name} (Home Stats)</h3>
                                <ul className="space-y-1">
                                    <li>Avg Goals For: {homeStats.avg_goals_for_home.toFixed(2)}</li>
                                    <li>Avg Goals Against: {homeStats.avg_goals_against_home.toFixed(2)}</li>
                                    <li>Avg Shots: {homeStats.avg_shots_home.toFixed(2)}</li>
                                    <li>Avg Shots on Target: {homeStats.avg_shots_on_target_home.toFixed(2)}</li>
                                    <li>Avg Corners: {homeStats.avg_corners_home.toFixed(2)}</li>
                                    <li>Avg Fouls: {homeStats.avg_fouls_home.toFixed(2)}</li>
                                    <li>Avg Yellows: {homeStats.avg_yellows_home.toFixed(2)}</li>
                                    <li>Avg Reds: {homeStats.avg_reds_home.toFixed(2)}</li>
                                </ul>
                            </div>

                            {/* Away Team Stats */}
                            <div>
                                <h3 className="text-lg font-semibold text-center mb-2">{awayTeam.name} (Away Stats)</h3>
                                <ul className="space-y-1">
                                    <li>Avg Goals For: {awayStats.avg_goals_for_away.toFixed(2)}</li>
                                    <li>Avg Goals Against: {awayStats.avg_goals_against_away.toFixed(2)}</li>
                                    <li>Avg Shots: {awayStats.avg_shots_away.toFixed(2)}</li>
                                    <li>Avg Shots on Target: {awayStats.avg_shots_on_target_away.toFixed(2)}</li>
                                    <li>Avg Corners: {awayStats.avg_corners_away.toFixed(2)}</li>
                                    <li>Avg Fouls: {awayStats.avg_fouls_away.toFixed(2)}</li>
                                    <li>Avg Yellows: {awayStats.avg_yellows_away.toFixed(2)}</li>
                                    <li>Avg Reds: {awayStats.avg_reds_away.toFixed(2)}</li>
                                </ul>
                            </div>
                        </div>
                    );
                })()}
            </div>
        </div>
    );
};

export default PredictForm;