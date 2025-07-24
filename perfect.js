// Snowfall Effect
const canvas = document.getElementById("snowfall");
const ctx = canvas.getContext("2d");

let width = (canvas.width = window.innerWidth);
let height = (canvas.height = window.innerHeight);

const numFlakes = 100;
const flakes = [];

function createFlakes() {
  for (let i = 0; i < numFlakes; i++) {
    flakes.push({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() * 4 + 1,
      d: Math.random() + 1,
    });
  }
}

function drawFlakes() {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "white";
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
    f.y += Math.pow(f.d, 2) + 1;
    f.x += Math.sin(f.y * 0.01);

    if (f.y > height) {
      flakes[i] = {
        x: Math.random() * width,
        y: 0,
        r: f.r,
        d: f.d,
      };
    }
  }
}

function resizeCanvas() {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
}

window.addEventListener("resize", resizeCanvas);
createFlakes();
setInterval(drawFlakes, 33);
