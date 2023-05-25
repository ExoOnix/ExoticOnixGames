// board stuff

var pxsize = 25;
var rows = 20;
var cols = 20;
var board;
var context;

var snakex = pxsize * 5;
var snakey = pxsize * 5;

var velx = 0;
var vely = 0;

var snake_body = [];

var foodx;
var foody;

var pts = 0;
var gameover = false;


window.onload = function () {
    board = document.getElementById('board');
    board.height = rows * pxsize;
    board.width = cols * pxsize;
    context = board.getContext('2d');
    placeFood();
    document.addEventListener("keyup", changeDirection);
    // update();
    setInterval(update, 1000 / 10); //100mils
}



function update() {
    if (gameover) {
        return;
    }

    context.fillStyle = 'green';
    context.fillRect(0, 0, board.width, board.height);

    context.fillStyle = 'red';
    context.fillRect(foodx, foody, pxsize, pxsize);

    if (snakex == foodx && snakey == foody) {
        snake_body.push([foodx, foody]);
        pts += 1;
        document.getElementById("pts").innerHTML = 'Points: ' + pts;
        placeFood();
    }

    for (let i = snake_body.length - 1; i > 0; i--) {
        snake_body[i] = snake_body[i - 1];
    }
    if (snake_body.length) {
        snake_body[0] = [snakex, snakey];
    }

    context.fillStyle = "black";
    snakex += velx * pxsize;
    snakey += vely * pxsize;
    context.fillRect(snakex, snakey, pxsize, pxsize);
    for (let i = 0; i < snake_body.length; i++) {
        context.fillStyle = 'lime';
        context.fillRect(snake_body[i][0], snake_body[i][1], pxsize, pxsize);
    }
    if (snakex < 0 || snakex > cols * pxsize || snakey < 0 || snakey > rows * pxsize) {
        gameover = true;
        alert("Game Over");
        location.reload();
    }
    for (let i = 0; i < snake_body.length; i++) {
        if (snakex == snake_body[i][0] && snakey == snake_body[i][1]) {
            gameover = true;
            alert("Game Over");
            location.reload();
        }
    }

}

function changeDirection(e) {
    if (e.code == 'ArrowUp' && vely != 1) {
        velx = 0;
        vely = -1;
    }
    else if (e.code == 'ArrowDown' && vely != -1) {
        velx = 0;
        vely = 1;
    }
    else if (e.code == 'ArrowLeft' && velx != 1) {
        velx = -1;
        vely = 0;
    }
    else if (e.code == 'ArrowRight' && velx != -1) {
        velx = 1;
        vely = 0;
    }
}


function placeFood() {
    foodx = Math.floor(Math.random() * cols) * pxsize;
    foody = Math.floor(Math.random() * rows) * pxsize;
}
