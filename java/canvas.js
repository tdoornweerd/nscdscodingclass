var canvas = document.querySelector('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var c = canvas.getContext('2d');


var gravity =1;
var friction = .80;

let mouse = {
    x: innerWidth / 2,
    y: innerHeight / 2
};


addEventListener('mousemove', function(event) {
    mouse.x = event.clientX;
    mouse.y = event.clientY
});

function random(max){
    var any = Math.floor(Math.random() * max)
    return any
}
function ranrange(min,max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}
class ball {
    constructor(x,y,radias,color) {
        this.x = x;
        this.y = y;
        this.radias = radias;
        this.color = color;
    }
    draw () {
        c.beginPath();
        c.arc(this.x,this.y,this.radias,0,Math.PI *2);
        c.fillStyle = this.color;
        c.fill();
        c.closePath();
    };
};

class gravityBall extends ball {
    constructor(x,y,radias,color,dy) {
        super(x,y,radias,color);
        this.dy = dy;
        this.update()
    }
    update() {
        if (this.y + this.radias > canvas.height ) {
            this.dy = -this.dy * friction;
            this.y = canvas.height - this.radias;
        } else {
            this.dy += gravity;
        }
        this.y += this.dy;
        this.draw()
    };
};

class mouseBall extends ball {
    constructor (x,y,radias,color) {
        super(x,y,radias,color)
        this.update()
    }
    update() {
        this.x = mouse.x;
        this.y = mouse.y;
        this.draw()
    }
};

let mouseCircle;
var balls;
var ballArray = [];
function init() {
    mouseCircle = new mouseBall(undefined,undefined,50,'green')
    /*=for (var i = 0; i < 100; i++) {
        var ranx = random(canvas.width);
        var rany = random(canvas.height)-75;
        var ranradias = random(75);
        var rancolor = 'rgb('+random(255)+', '+random(255)+', '+random(255)+')'
        var ranspeed = ranrange(30,30)
        ballArray.push(new gravityBall(ranx,rany,ranradias,rancolor,ranspeed))
    };*/
    balls = new gravityBall(300,canvas.height-700,50,'red',10)
};


function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0,0,canvas.width,canvas.height);
    for (var i = 0; i < ballArray.length; i++) {
        ballArray[i].update();
    };
    mouseCircle.update()
    balls.update();
};

init();
animate();
