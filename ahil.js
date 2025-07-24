const canvas = document.getElementById("snowfall");
const ctx = canvas.getContext("2d");

let width = window.innerWidth;
let height = window.innerHeight;
canvas.width = width;
canvas.height = height;

let numFlakes = 150;
let flakes = [];

function createFlakes() {
  for (let i = 0; i < numFlakes; i++) {
    flakes.push({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() * 3 + 1,
      d: Math.random() + 1
    });
  }
}

function drawFlakes() {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "#fff";
  ctx.beginPath();
  for (let i = 0; i < numFlakes; i++) {
    const f = flakes[i];
    ctx.moveTo(f.x, f.y);
    ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2, true);
  }
  ctx.fill();
  moveFlakes();
}

function moveFlakes() {
  for (let i = 0; i < numFlakes; i++) {
    const f = flakes[i];
    f.y += f.d;
    f.x += Math.sin(f.y * 0.01);

    if (f.y > height) {
      flakes[i] = {
        x: Math.random() * width,
        y: 0,
        r: f.r,
        d: f.d
      };
    }
  }
}

function updateFlakes() {
  drawFlakes();
  requestAnimationFrame(updateFlakes);
}

window.addEventListener("resize", () => {
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;
});

createFlakes();
updateFlakes();
