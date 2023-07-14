// Global Variables
const btnPhone = document.querySelector("#phone");
const btnEmail = document.querySelector("#email");
const devEmail = document.querySelector("#devEmail");

function copyToClipboard(icon){
    let phoneNumber = 7804927157;
    let email = 'kloepelm@ualberta.ca';
    let devEmail = 'ncw1@ualberta.ca';

    // 1) Check if icon is the phone or email.
    // 2) Check if browser is "inSecureContext". Then you can use the navigator clipboard method.
    // 3) Otherwise, use the deprecated "document.execCommand" method.

    if (icon === "phone"){
        if (navigator.clipboard && window.isSecureContext){
            navigator.clipboard.writeText(phoneNumber)
            // Sucessfully copies to clipboard.
            .then(function(){
                showSnackBar();
                console.log("Phone number copied to clipboard.");
            })
            // Failed to copy.
            .catch(function(error){
                console.error("Failed to copy phone number.");
            })
        }
        else{
            showSnackBar();
            var tempInput = document.createElement("input");
            tempInput.setAttribute("value", phoneNumber);
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
            console.log("Copied phone number!");
        }

    }
    else if (icon === "email"){
        if (navigator.clipboard && window.isSecureContext){
            navigator.clipboard.writeText(email)
            .then(function(){
                showSnackBar();
                console.log("Email copied to clipboard.");
            })
            .catch(function(error){
                console.error("Failed to copy email.");
            })
        }
        else{
            showSnackBar();
            var tempInput = document.createElement("input");
            tempInput.setAttribute("value", email);
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
            console.log("copied email!");
        }
    }
    // Dev email (mine)
    else if (icon === "devEmail"){
        if (navigator.clipboard && window.isSecureContext){
            navigator.clipboard.writeText(devEmail)
            .then(function(){
                showSnackBar();
                console.log("Email copied to clipboard.");
            })
            .catch(function(error){
                console.error("Failed to copy email.");
            })
        }
        else{
            showSnackBar();
            var tempInput = document.createElement("input");
            tempInput.setAttribute("value", devEmail);
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
            console.log("copied email!");
        }
    }
}

function showSnackBar(){
    var notif = document.querySelector("#snackbar");
    notif.className="show";
    setTimeout(()=>{
        notif.className = notif.className.replace("show", "");}, 3000);
}

function main(){
    console.log("the javascript file is lnked");

    // Click listeners
    btnPhone.addEventListener("click", () =>{
        copyToClipboard("phone");
    });
    btnEmail.addEventListener("click", () => {
        copyToClipboard("email");
    })
    devEmail.addEventListener("click", () => {
        copyToClipboard("devEmail");
    })

}

main();