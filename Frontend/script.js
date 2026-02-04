document.querySelector('#predictForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // prevent page reload

    const data = {
        batting_team: document.querySelector('#battingTeam').value,
        bowling_team: document.querySelector('#bowlingTeam').value,
        city: document.querySelector('#city').value,
        total_run_x: parseInt(document.querySelector('#total_run_x').value),
        current_score: parseInt(document.querySelector('#current_score').value),
        overs_completed: parseFloat(document.querySelector('#overs_completed').value),
        wicket_fallen: parseInt(document.querySelector('#wicket_fallen').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();

        
        document.querySelector('#result').innerHTML = `
            <div class="title">WIN PROBABILITY</div>
            <div class="teams">
              <span>${data.batting_team}: ${result.Probability.batting_team}%</span>
              <span>${data.bowling_team}: ${result.Probability.bowling_team}%</span>
             </div>
             <div class="progress-bar">
             <div class="batting-bar" style="width: ${result.Probability.batting_team}%;"></div>
            <div class="bowling-bar" style="width: ${result.Probability.bowling_team}%;"></div>
        </div>
            `;
    } 
    catch (err) {
        console.error(err);
        document.querySelector('#result').innerHTML = `
    <div style="text-align: center; color: #ff4d4f; font-weight: bold; font-size: 18px;">
        Something Went Wrong!!!
    </div>
`;

    }
});
