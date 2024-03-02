const search=document.querySelector('input');
const button=document.querySelector('button');
button.addEventListener('click',()=>{
    button.classList.toggle('active');
    search.classList.toggle('active');
    search.focus();
})