// Global Variables
const body = document.body;
const container = document.querySelector(".container");
const btn_changeSize = document.querySelector("#btn_changeSize");
const btn_changeColor = document.querySelector("#btn_changeColor");
const btn_resetColor = document.querySelector("#btn_resetColor");
const colorPicker = document.querySelector("#colorPicker");
const currentColor = document.querySelector("#currentColor");

// Function that creates the divs. Default is 16 x 16.
// This function will also set the correct CSS layouts.
function createDivs(x = 16){
    for (let i = 0; i < (x); i++){
        const row = document.createElement('div'); 
        row.classList.add("row");
        container.appendChild(row);

        for (let j = 0; j < x; j++){
            const cell = document.createElement('div'); // 'td' = table data.
            // Give the cell properties.
            cell.classList.add('cell');
            cell.addEventListener('mouseover', () => {
                cell.setAttribute('style', 'background-color: ' + colorPicker.value + ';');
            });
            
            //cell.innerText = "cell";
            row.appendChild(cell);
        }   
    }
}

// Button: Resize grid.
function divSize(){
    size = prompt("Enter size of the grid (0 - 19): ");

    while (size > 19){
        const invalid = size;
        size = prompt(invalid + " is an invalid grid size. Input a valid number between 0 - 19.")
    }

    // Wipe the original grid.
    while (container.firstChild){
        container.removeChild(container.firstChild);
    }

    createDivs(size);
}

// Button: Change hover color.
function changeColor(){
    const allCells = Array.from(document.querySelectorAll('.cell'));
    colorPicker.click(); // Opens the color picker (default hidden)
    
    allCells.forEach((cell) => {
        cell.addEventListener('mouseover', () => {
            cell.setAttribute('style', 'background-color: ' + colorPicker.value + ';');
        })
    });
    
}


// Button: Reset the grid color to blank.
function resetColor(){
    const allCells = Array.from(document.querySelectorAll('.cell'));
    allCells.forEach((cell) => {
        cell.setAttribute('style', 'background-color: beige');
    });
    // for (let i = 0; i < allCells.length; i++){
    //     allCells[i].setAttribute('style', 'background-color:white');
    // }
}

function main(){
    // Initial state.
    createDivs();

    // Event listeners.
    btn_changeSize.addEventListener('click', divSize);
    btn_changeColor.addEventListener('click', changeColor);
    btn_resetColor.addEventListener('click', resetColor);

    


}

main();

