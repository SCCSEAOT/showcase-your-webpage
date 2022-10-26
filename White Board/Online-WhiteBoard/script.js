const ctx = document.getElementById('canvas').getContext('2d'); //creating a 2D canvas
window.addEventListener('resize', resize); 
resize();
let mousePos = { //initially x and y position
  x:0,
  y:0
}
window.addEventListener('mousemove', draw); //to draw
window.addEventListener('mousedown', mousePosition); 
window.addEventListener('mouseenter', mousePosition);

function mousePosition(e) { //positioning the mouse as per client
  mousePos.x = e.clientX;
  mousePos.y = e.clientY;
}

function resize() { //canvas resize
  ctx.canvas.width = window.innerWidth;
  ctx.canvas.height = window.innerHeight;
}

function draw(e) {
  if(e.buttons !== 1) //is nothing is drawn then no response
    return;
  ctx.beginPath(); //to start
  ctx.lineCap = 'round'; //starting head of a line
  ctx.strokeStyle = '#111'; //black colour
  ctx.linewidth = '5';
  ctx.moveTo(mousePos.x, mousePos.y); //to move the mouse n x and y psition
  mousePosition(e); 
  ctx.lineTo(mousePos.x, mousePos.y);
  ctx.stroke(); //while pressing the mouse to draw
}