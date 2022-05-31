const hamburger = document.querySelector('.header .navbar .nav-list .hamburger');
const mobile_menu = document.querySelector('.header .navbar .nav-list ul');
const header = document.querySelector('.header .container');

hamburger.addEventListener('click',()=>{
    if(hamburger.classList.contains('deactive') && mobile_menu.classList.contains('deactive')){
        hamburger.classList.remove('deactive');
        mobile_menu.classList.remove('deactive');
    }
    else{
        hamburger.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    }
});


// const x = document.querySelector('.header .navbar .nav-list .hamburger');
// const z = document.querySelector('.header .navbar .nav-list ul');
const y = document.querySelectorAll('.menu');
const mediaQuery = window.matchMedia("(min-width:1020px)");
if(window.innerWidth < 1021){
    for(let i = 0;i<y.length;i++){
        y[i].addEventListener('click',()=>{
            hamburger.classList.toggle('deactive');
            mobile_menu.classList.toggle('deactive');
        });
    }
}



var faq = document.getElementsByClassName("faq-page");
var i;
for(i = 0;i<faq.length;i++){
    faq[i].addEventListener("click",function(){
        this.classList.toggle("active");

        var body = this.nextElementSibling;
        if(body.style.display == "block"){
            body.style.display = "none";
        }else{
            body.style.display = "block";
        }
    });
}

