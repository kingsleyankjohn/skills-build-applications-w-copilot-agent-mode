import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Leaderboard API endpoint:', API_URL);
        console.log('Fetched leaderboard:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaderboard.map((entry, idx) => (
          <li className="list-group-item" key={idx}>
            {entry.user} ({entry.team}) - Score: {entry.score}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
