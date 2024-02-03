function randCol(){
    const red=Math.floor(Math.random()*256);
    const green=Math.floor(Math.random()*256);
    const blue=Math.floor(Math.random()*256);
    const col=`rgb(${red},${green},${blue})`;
    return col;
}
let a;
function bgCol(){
    document.body.style.backgroundImage=``;
    a=randCol();
    document.body.style.backgroundColor =a;
}

function bgGrad(){
    //document.body.style.backgroundColor =randCol();
    const b=randCol();
    document.body.style.backgroundImage=`linear-gradient(to right, ${a} ,${b} )`;
}

function btCol(){
    const allButtons=document.getElementsByTagName('button');
    for(let i=0;i<allButtons.length;i++){
        allButtons[i].style.backgroundColor=a;
    }
}