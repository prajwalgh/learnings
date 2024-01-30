const currentDate=new Date();
document.getElementById("Date").innerHTML=currentDate;
var age;

function getAge(){
 const userInput=document.getElementById("dob").value;
 const userDob=new Date(userInput);
 if ( userDob.getMonth()>=currentDate.getMonth()){
    age=currentDate.getFullYear()-userDob.getFullYear()+1;
   }
else{
        age=currentDate.getFullYear()-userDob.getFullYear();

}
 document.getElementById("age").innerHTML=age;
 document.getElementsByClassName("Container2")[0].style.zIndex=2;}