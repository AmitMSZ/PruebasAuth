console.log('js ok')

window.addEventListener('load', function() {

    const   form = document.querySelector('.ctn-form'), 
            show = form.querySelector(".show-me"), 
            getPassType = form.querySelector('.input-password');

    show.addEventListener("click", () => {
        console.log(getPassType)

        if (show.textContent === 'show') {
            show.textContent = 'hide'
            getPassType.setAttribute('type', 'text')
            } else {
            show.textContent = 'show'
            getPassType.setAttribute('type', 'password')
            }
    })

});