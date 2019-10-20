console.log("connected");

function getColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

var headerOne = document.querySelector("#one");
var headerTwo = document.querySelector("#two");
var headerThree = document.querySelector("#three");

headerOne.addEventListener("mouseover", function(){
  headerOne.textContent = "Mouse Over";
  headerOne.style.color = "blue";
})

headerOne.addEventListener("mouseout", function(){
  headerOne.textContent = "hoover over me";
  headerOne.style.color = "purple";
})

headerTwo.addEventListener("click", function(){
  var color = getColor()
  headerTwo.style.color = color;
  headerTwo.textContent = "color: " + color;
})
