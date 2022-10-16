let k='sdf';
let r = k.slice(0,-1);
console.log(r);

//intialise
let num='';
let n;
let ans=0;
let optn;
let num1,num2;
const buttons = document.querySelectorAll('.num');
const input = document.querySelector('.input');
const subInput = document.querySelector('.sub-input')
const equal = document.querySelector('.equal');
const opn = document.querySelectorAll(".operation");
const delBtn = document.querySelector(".del");
const clrBtn = document.querySelector('.clr');

//operations
const add = function(a,b){
    input.value=a+b;
}

const sub = function(a,b){
    input.value= a-b;
}

const mul = function(a,b){
    input.value=a*b;
}

const div = function(a,b){
    input.value=a/b;
}

const per = function(a,b){
    input.value=(a/100)*b;
}

const del = function(){
    console.log(input.value);
    n=input.value
    console.log(n);
    console.log(n.slice(0,-1))    
    input.value=n.slice(0,-1);
}

const clr = function(){
    input.value='';
    subInput.value='';
}


//Data entry
buttons.forEach(ele => ele.addEventListener('click',function(){
    num = input.value + ele.value;
    input.value=num;
}));


//operations execution
opn.forEach(el => el.addEventListener('click',function(){
    opn.forEach(ela => ela.classList.remove('btn-active'));
    optn=el.value;
    el.classList.add('btn-active');
    console.log(input.value);
    num1=Number(input.value);
    subInput.value=input.value;
    input.value='';
    console.log(optn);
}));


//del clr
delBtn.addEventListener('click',function(){
    del();
})

clrBtn.addEventListener('click',function(){
    clr();
})


//result
equal.addEventListener("click",function(){
    num2=Number(input.value);
    console.log(input.value);
    console.log(optn);
    opn.forEach(ela => ela.classList.remove('btn-active'));
    if(optn=='+'){
        console.log("asdf");
        add(num1,num2);
    }
    else if(optn=='-'){
        sub(num1,num2);
    }
    else if(optn=='*'){
        mul(num1,num2);
    }
    else if(optn=='/'){
        div(num1,num2);
    }
    else if(optn=='%'){
        
        console.log("asdf");
        per(num1,num2);
    }
    subInput.value =subInput.value + optn + num2;
});

