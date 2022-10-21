var noOfKeys = document.querySelectorAll(".note").length;

for (var i = 0; i < noOfKeys; i++) {
  document.querySelectorAll(".note")[i].addEventListener("click", function() {
    var buttonInnerHTML = this.innerHTML;
    makeSound(buttonInnerHTML);
    buttonAnimation(buttonInnerHTML);
  });
}
document.addEventListener("keypress", function(event) {
  makeSound(event.key);
  buttonAnimation(event.key);
});

function makeSound(key) {

    if(key=="sa" || key=="s"){
      var tom1 = new Audio("sounds/sa.mp3");
      tom1.play();
    }

    else if(key=="re" || key=="d"){
      var tom2 = new Audio("sounds/re.mp3");
      tom2.play();
    }

    else if(key=="ga" || key=="f"){
      var tom3 = new Audio("sounds/ga.mp3");
      tom3.play();
    }

    else if(key=="ma" || key=="g"){
      var tom4 = new Audio('sounds/ma.mp3');
      tom4.play();
    }

    else if(key=="pa" || key=="h"){
      var snare = new Audio('sounds/pa.mp3');
      snare.play();
    }

    else if(key=="dha" || key=="j"){
      var crash = new Audio('sounds/dha.mp3');
      crash.play();
    }

    else if(key=="ni" || key=="k"){
      var kick = new Audio('sounds/ni.mp3');
      kick.play();
    }

    else if(key=="saa" || key=="l"){
      var kick = new Audio('sounds/saa.mp3');
      kick.play();
    }
    else console.log(key);
  }

function buttonAnimation(currentKey) {
  var activeButton = document.querySelector("." + currentKey);
  activeButton.classList.add("pressed");
  setTimeout(function() {
    activeButton.classList.remove("pressed");
  }, 100);
}
