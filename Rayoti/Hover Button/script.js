const container = document.getElementById("container");
const colors = ["#95FA03", "#00FAF7", "#FA00D0", "#FFAE00", "#3800AF"];
const SQUARES = 2700;

const getRandomColor = () => colors[Math.floor(Math.random() * colors.length)];

const setColor = (square) => {
  const color = getRandomColor();
  square.style.background = color;
  square.style.boxShadow = `0 0 2px ${color}, 0 0 10px ${color}`;
};

const removeColor = (square) => {
  square.style.background = "#ldldld";
  square.style.boxShadow = "0 0 2px #000";
};

for(let i = 0; i < SQUARES; i++) {
  const square = document.createElement("div");
  square.classList.add("square");
  square.addEventListener("mouseover", () => setColor(square));
  square.addEventListener("mouseout", () => removeColor(square));
  container.appendChild(square);
}

