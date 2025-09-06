// document.addEventListener('DOMContentLoaded', function() {
//     // Get initial data from server
//     function fetchGameState() {
//         fetch('/get-game-state-json/')
//             .then(response => response.json())
//             .then(data => {
//                 updateDisplay(data);
//                 startCountdown(data);
//             })
//             .catch(error => console.error('Error:', error));
//     }

//     function updateDisplay(data) {
//         document.getElementById("team-red-name").innerText = data.team_red_name + ":";
//         document.getElementById("team-blue-name").innerText = data.team_blue_name + ":";
//         document.getElementById("team-red-score").innerText = data.team_red_score;
//         document.getElementById("team-blue-score").innerText = data.team_blue_score;
//         document.getElementById("round-number").innerText = data.round_number;
//         document.getElementById("game-timer").innerText = formatTime(data.game_time);
//         document.getElementById("penalty-timer").innerText = formatTime(data.penalty_time);
//     }

//     function formatTime(seconds) {
//         let mins = Math.floor(seconds / 60);
//         let secs = seconds % 60;
//         return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
//     }

//     function startCountdown(initialData) {
//         let gameTime = initialData.game_time;
//         let penaltyTime = initialData.penalty_time;
//         let gameRunning = initialData.game_running;
//         let penaltyRunning = initialData.penalty_running;

//         // Update countdown every second
//         setInterval(() => {
//             if (gameRunning && gameTime > 0) {
//                 gameTime--;
//                 document.getElementById("game-timer").innerText = formatTime(gameTime);
//             }
            
//             if (penaltyRunning && penaltyTime > 0) {
//                 penaltyTime--;
//                 document.getElementById("penalty-timer").innerText = formatTime(penaltyTime);
//             }
//         }, 1000);

//         // Refresh data from server every 2 seconds to sync with admin changes
//         setInterval(() => {
//             fetch('/get-game-state-json/')
//                 .then(response => response.json())
//                 .then(data => {
//                     gameRunning = data.game_running;
//                     penaltyRunning = data.penalty_running;
                    
//                     // Only update times if they're different from our current countdown
//                     if (data.game_time !== gameTime) {
//                         gameTime = data.game_time;
//                         document.getElementById("game-timer").innerText = formatTime(gameTime);
//                     }
                    
//                     if (data.penalty_time !== penaltyTime) {
//                         penaltyTime = data.penalty_time;
//                         document.getElementById("penalty-timer").innerText = formatTime(penaltyTime);
//                     }
//                 })
//                 .catch(error => console.error('Error:', error));
//         }, 2000);
//     }

//     // Initialize
//     fetchGameState();
// });


function formatTime(seconds) {
    let mins = Math.floor(seconds / 60);
    let secs = seconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
}

// Auto refresh the page every second to show real-time updates
setInterval(function() {
    location.reload();
}, 1000);