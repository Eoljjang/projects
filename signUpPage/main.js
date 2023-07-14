
const form = document.querySelector("#signupForm");
const snackbar = document.querySelector("#snackbar");

function showSnackBar(){
    var notif = document.querySelector("#snackbar");
    notif.className="show";
    setTimeout(()=>{
        notif.className = notif.className.replace("show", "");}, 3000);
}

function showInvalidSnackBar(){
    var notif = document.querySelector("#snackbar-invalid");
    notif.className="show";
    setTimeout(()=>{
        notif.className = notif.className.replace("show", "");}, 3000);
}

form.addEventListener("submit", function(e) {
    e.preventDefault(); // Prevents form submission.

    const password = document.querySelector('#password');
    const passwordValue = document.querySelector('#password').value;
    const confirmPassword = document.querySelector('#confirmPassword');
    const confirmPasswordValue = document.querySelector('#confirmPassword').value;

    // Check that passwords are the same //
    if (passwordValue !== confirmPasswordValue){
        showInvalidSnackBar();
        password.classList.add("invalid-input");
        confirmPassword.classList.add("invalid-input");

    }
    // Valid, is submitted, and we clear the form.
    else{
        showSnackBar();
        password.classList.remove("invalid-input");
        confirmPassword.classList.remove("invalid-input");
        form.reset();
    }
})
