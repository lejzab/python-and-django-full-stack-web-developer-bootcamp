console.log('Witaj');

var restart = document.querySelector("#b");
var squares = document.querySelectorAll("td");

function clearBoard(){
  for (square of squares) {
    square.textContent = "";
  }
}

function changeMarker() {
  if(this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else {
    this.textContent = "";
  }
}

restart.addEventListener("click", clearBoard);

for (square of squares) {
  square.addEventListener("click", changeMarker);
}
