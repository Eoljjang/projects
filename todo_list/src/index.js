import './style.css';
let timer;
let minutes = 25; // Defaults to 25 minutes.
let seconds = 0;
let isPaused = true; // By default, the timer is "paused".
let enteredTime = null; // User has not entered a specific time frame.
let stop_red = "#ff7a61";
const restart_timer_btn = document.querySelector("#restart-timer-btn");
const choose_time_btn = document.querySelector("#choose-time-btn");
const toggle_timer_btn = document.querySelector("#toggle-timer-btn");
const pomodoro = document.querySelector(".pomodoro-timer");
const timer_circle = document.querySelector(".timer-circle");
const add_task_btn = document.querySelector("#add-task-btn");
const task_container = document.querySelector("#task-container");
const checkboxes = document.querySelector(".task-checkbox");


function startTimer() {
    // Every second, calls the updateTimer() function. 
    timer = setInterval(updateTimer, 1000);
}

function updateTimer() {
    // 1) Every second, gets the timer element on the screen.
    const timerElement = document.querySelector("#timer");

    // 2) Sets its textContent to be the current timer remaining.
    timerElement.textContent = formatTime(minutes, seconds); 

    // 3) Check if timer has been compelted.
    if (minutes === 0 && seconds === 0){
        clearInterval(timer); // 3.1) Stop updating the timer.
        alert("Time is up, take a break!");
    }

    // 4) If timer is NOT paused.
    else if (!isPaused){
        // 4.1) You're in the current minute -> decrement the seconds.
        if (seconds > 0){
            seconds--;
        }
        // 4/2) You've cycled into a new minute -> Restart the seconds and decerement the minutes.
        else{
            seconds = 59;
            minutes--;
        }
    }
}

function formatTime(minutes, seconds){
    // Given the current minutes & seconds remaining, format the time nicely.
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`; 
}

// WHEN TOGGLE BUTTON IS CLICKED (toggles between 'started' and 'paused' modes).
toggle_timer_btn.addEventListener("click", () => {
    // Take the negated value since it's a toggle. IE: switch between pause and unpaused.
    isPaused = !isPaused;

    if (isPaused){
        clearInterval(timer); // Stop updating the timer.
        toggle_timer_btn.textContent = 'Start'; 
        toggle_timer_btn.style.backgroundColor = "#6af1a3"; // start = green;
        timer_circle.style.borderColor = "#6af1a3";
    }
    else{ // Unpausing
        startTimer();
        toggle_timer_btn.textContent = "Pause";
        console.log('paused');
        toggle_timer_btn.style.backgroundColor = "#ff7a61"; // pause = red.
        timer_circle.style.borderColor = "#ff7a61";
        
    }
})

// WHEN RESTART BUTTON IS CLICKED
restart_timer_btn.addEventListener("click", () => {
    clearInterval(timer); // Stop updating the timer.
    minutes = enteredTime || 25; // Either sets it to the user inputted time, or default 25 minutes.
    seconds = 0;
    isPaused = true;

    // Reset everything about the timer
    const timerElement = document.querySelector("#timer");
    timerElement.textContent = formatTime(minutes, seconds);

    toggle_timer_btn.textContent = 'Start'; 
    toggle_timer_btn.style.backgroundColor = "#6af1a3"; // set start = green.
    timer_circle.style.borderColor = "#6af1a3"; 
})

// WHEN CHOOSE TIME BUTTON IS CLICKED
choose_time_btn.addEventListener("click", () => {
    const newTime = prompt("Enter new time in minutes"); // Get user input.

    if (!isNaN(newTime) && newTime > 0){ // Check input data integrity.
        enteredTime = parseInt(newTime); // Convert user input to integer.
        minutes = enteredTime;
        seconds = 0;
        isPaused = true;

        const timerElement = document.querySelector("#timer");
        timerElement.textContent = formatTime(minutes, seconds);
        clearInterval(timer); // Get rid of any old updates.

        // Make sure the start button is green again.
        toggle_timer_btn.textContent = 'Start';
        toggle_timer_btn.style.backgroundColor = "#6af1a3";
        timer_circle.style.borderColor = "#6af1a3";
    }
    else{
        alert("Invalid input. Must be a number greater than 0.");
    }
})

// LOCAL STORAGE: Checks if local storage is available //
function storageAvailable(type) {
    let storage;
    try {
      storage = window[type];
      const x = "__storage_test__";
      storage.setItem(x, x);
      storage.removeItem(x);
      return true;
    } catch (e) {
      return (
        e instanceof DOMException &&
        // everything except Firefox
        (e.code === 22 ||
          // Firefox
          e.code === 1014 ||
          // test name field too, because code might not be present
          // everything except Firefox
          e.name === "QuotaExceededError" ||
          // Firefox
          e.name === "NS_ERROR_DOM_QUOTA_REACHED") &&
        // acknowledge QuotaExceededError only if there's something already stored
        storage &&
        storage.length !== 0
      );
    }
  }

// ADDING TASKS //
add_task_btn.addEventListener("click", () =>{
    add_task();
})

function add_task(){
    // 1) create task item div
    const task_item = document.createElement("div");
    task_item.classList.add("task-item");

    // 2) Add the input field.
    const task_input = document.createElement("input");
    task_input.classList.add("task-text");
    task_item.appendChild(task_input);

    // 3) Add the checkbox field.
    const task_checkbox = document.createElement("input");
    task_checkbox.type = 'checkbox';
    task_checkbox.classList.add("task-checkbox");
    task_item.appendChild(task_checkbox);

    // 4) Add the task item into the task container
    task_container.appendChild(task_item);
}