// Global
const choices = Array("rock", "paper", "scissors");
let results = 0;
let results_CPU = 0;

// Variabls we have to update text for
const CPU_points = document.getElementById("CPU");
const CPU_choice = document.getElementById("CPU_choice");
const Player_points = document.getElementById("User");
const Player_choice = document.getElementById("user_choice");
const outcome = document.getElementById("outcome");

// function getPlayerChoice(){
//     let p_move = prompt("Enter a move");

//     // Check that input isn't empty.
//     if (p_move.length == 0){
//         throw console.log("Input can't be empty"); // Terminates script. Refresh page to re-run.
//     }

//     // Convert it to lower case.
//     p_move = p_move.toLowerCase();

//     // Check that it is RPS.
//     if (choices.includes(p_move)){
//         playRound(p_move, getComputerChoice());
//     }
//     else{
//         throw console.log("Invalid input.");
//     }
// }

function getComputerChoice(){
    // Retrieves a random index of the list.
    var randomIndex = Math.floor(Math.random() * choices.length);

    // Use that index to retrieve a random choice
    return choices[randomIndex];
}

function playRound(p_move, c_move){
    Player_choice.innerHTML = "You chose: " + p_move;
    CPU_choice.innerHTML = "CPU chose: " + c_move;


    if (p_move === "rock"){
        if (c_move === "rock"){
            outcome.innerHTML = "TIE";
        }
        else if (c_move === "paper"){
            outcome.innerHTML = "You lost!";
            results_CPU += 1;
            CPU_points.innerHTML = "Computer: " + results_CPU;
        }
        else if (c_move === "scissors"){
            outcome.innerHTML = "You won!";
            results += 1;
            Player_points.innerHTML = "You: " + results;
        }
    }

    else if (p_move === "paper"){
        if (c_move === "paper"){
            outcome.innerHTML = "TIE";
        }
        else if (c_move === "scissors"){
            outcome.innerHTML = "You lost!";
            results_CPU += 1;
            CPU_points.innerHTML = "Computer: " + results_CPU;
        }
        else if (c_move === "rock"){
            outcome.innerHTML = "You won!";
            results += 1;
            Player_points.innerHTML = "You: " + results;
        }
    }

    else if (p_move === "scissors"){
        if (c_move === "scissors"){
            outcome.innerHTML = "TIE";
        }
        else if (c_move === "rock"){
            outcome.innerHTML = "You lost!";
            results_CPU += 1;
            CPU_points.innerHTML = "Computer: " + results_CPU;
        }
        else if (c_move === "paper"){
            outcome.innerHTML = "You won!";
            results += 1;
            Player_points.innerHTML = "You: " + results;
        }
    }
    if (results === 5){
        document.getElementById("final_result").textContent="You won! Yahoo";
    }
    else if (results_CPU === 5){
        document.getElementById("final_result").textContent="CPU won :(";
    }

}

function main(){
    // Set listeners for all the buttons
    document.getElementById("rock").setAttribute("onClick", "javascript: playRound('rock', getComputerChoice());");
    document.getElementById("paper").setAttribute("onClick", "javascript: playRound('paper', getComputerChoice());");
    document.getElementById("scissors").setAttribute("onClick", "javascript: playRound('scissors', getComputerChoice());");



}

main();