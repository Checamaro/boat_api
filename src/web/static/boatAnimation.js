const canvas = document.getElementById("boatCanvas");
const ctx = canvas.getContext("2d");

let boat = {
    x: canvas.width / 2,
    y: canvas.height - 50,
    direction: "stopped",
    passengers: 0,
    paddleAngle: 0,
    paddleRotationSpeed: 0.15
};

// Функция отрисовки лодки и весла
function drawBoat(ctx) {
    ctx.fillStyle = "brown";

    let x = boat.x;
    let y = boat.y;
    let widthTop = 100;
    let widthBottom = 60;
    let height = 40;

    // Отрисовка перевёрнутой трапеции (лодки)
    ctx.beginPath();
    ctx.moveTo(x - widthTop / 2, y - height);
    ctx.lineTo(x + widthTop / 2, y - height);
    ctx.lineTo(x + widthBottom / 2, y);
    ctx.lineTo(x - widthBottom / 2, y);
    ctx.closePath();
    ctx.fill();

    // Отрисовка пассажиров (круги над лодкой)
    ctx.fillStyle = "black";
    for (let i = 0; i < boat.passengers; i++) {
        let px = x - (boat.passengers - 1) * 10 + i * 20;
        let py = y - height - 10;
        ctx.beginPath();
        ctx.arc(px, py, 5, 0, Math.PI * 2);
        ctx.fill();
    }

    // Точка крепления весла (верхнее основание трапеции)
    let paddleCenterX = x;
    let paddleCenterY = y - height;
    let paddleLength = widthTop * 0.65;

    // Вычисление координат концов весла
    let paddleX1 = paddleCenterX - Math.cos(boat.paddleAngle) * paddleLength;
    let paddleY1 = paddleCenterY - Math.sin(boat.paddleAngle) * paddleLength;
    let paddleX2 = paddleCenterX + Math.cos(boat.paddleAngle) * paddleLength;
    let paddleY2 = paddleCenterY + Math.sin(boat.paddleAngle) * paddleLength;

    // Отрисовка весла (палочки)
    ctx.strokeStyle = "black";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(paddleX1, paddleY1);
    ctx.lineTo(paddleX2, paddleY2);
    ctx.stroke();
}

// Функция обновления позиции лодки
function updateBoatPosition() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (boat.direction === "forward" && boat.y > 50) boat.y -= 5;
    if (boat.direction === "backward" && boat.y < canvas.height - 50) boat.y += 5;
    if (boat.direction === "left" && boat.x > 50) boat.x -= 5;
    if (boat.direction === "right" && boat.x < canvas.width - 50) boat.x += 5;

    // Анимация весла
    if (boat.direction !== "stopped") {
        boat.paddleAngle += boat.paddleRotationSpeed;
    }

    drawBoat(ctx);
    requestAnimationFrame(updateBoatPosition);
}

// Функция отправки команд на сервер
function sendCommand(endpoint, callback) {
    const API_BASE_URL = "http://127.0.0.1:5000";
    fetch(`${API_BASE_URL}${endpoint}`, { method: "POST" })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (callback) callback(data);
        })
        .catch(error => console.error("Ошибка:", error));
}

// Движение лодки
function move(direction) {
    sendCommand(`/move/${direction}`, () => {
        boat.direction = direction;

        // Меняем направление вращения весла
        if (direction === "forward" || direction === "right") {
            boat.paddleRotationSpeed = 0.15;
        } else if (direction === "backward" || direction === "left") {
            boat.paddleRotationSpeed = -0.15;
        }

        updateUI();
    });
}

// Остановка лодки
function stopBoat() {
    sendCommand("/stop", () => {
        boat.direction = "stopped";
        boat.paddleRotationSpeed = 0;
        updateUI();
    });
}

// Добавление пассажира
function addPassenger() {
    sendCommand("/passenger/add", (data) => {
        if (!data.error) {
            boat.passengers++;
            updateUI();
        }
    });
}

// Удаление пассажира
function removePassenger() {
    sendCommand("/passenger/remove", (data) => {
        if (!data.error && boat.passengers > 0) {
            boat.passengers--;
            updateUI();
        }
    });
}

// Обновление UI
function updateUI() {
    document.getElementById("passengerCount").textContent = boat.passengers;
    document.getElementById("boatDirection").textContent = boat.direction === "stopped" ? "Остановлено" : boat.direction;
}

// Инициализация
updateUI();
drawBoat(ctx);
updateBoatPosition();
