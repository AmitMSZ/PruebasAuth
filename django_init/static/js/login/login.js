
window.addEventListener('load', function() {

    const   form = document.querySelector('.ctn-form'), 
            show = form.querySelector(".show-me"), 
            getPassType = form.querySelector('.input-password');

    const errorMessage = !document.getElementById("message-error");
    console.log(errorMessage);
    if (!errorMessage) {
        setTimeout(()=>{
            document.getElementById("message-error").style.display = "none";
        }, 5000)
    }

    show.addEventListener("click", () => {
        
        if (show.textContent === 'show') {
            show.textContent = 'hide'
            getPassType.setAttribute('type', 'text')
            } else {
            show.textContent = 'show'
            getPassType.setAttribute('type', 'password')
            }
    })

});