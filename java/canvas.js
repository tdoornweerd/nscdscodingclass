var canvas = document.querySelector('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var c = canvas.getContext('2d');


var gravity =1;
var yfriction = .93;
var xfriction = .97;
var distancetillmove = 100;
var moveddistance = 30;

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
    constructor(x,y,radias,color,dy,dx) {
        super(x,y,radias,color);
        this.dy = dy;
        this.dx = dx;
        this.update()
    };
    update() {
        if (this.y + this.radias > canvas.height ) {
            this.dy = -this.dy * yfriction;
            this.y = canvas.height - this.radias;
            console.log(this.dy, this.y);
        } else {
            this.dy += gravity;
        };
        this.y += this.dy;
        
        if (this.x + this.radias > canvas.width || this.x - this.radias < 0) {
            this.dx = -this.dx * xfriction;
        }
        this.x += this.dx;
        this.draw()
    };
    tooclose() {
        this.dy = moveddistance;
    }
};

class mouseBall extends ball {
    constructor (x,y,radias,color) {
        super(x,y,radias,color)
        this.update()
    };
    update() {
        this.x = mouse.x;
        this.y = mouse.y;
        this.draw()
    };
};

function getDistance (x1,y1,movedball) {
    let xdistance = movedball.x - x1;
    let ydistance = movedball.y - y1;
    totalDistance = Math.sqrt(Math.pow(xdistance,2) + Math.pow(ydistance,2));
    if (totalDistance < distancetillmove) {
        movedball.tooclose()
    }
};

let mouseCircle;
var balls;
var ballArray = [];
function init() {
    mouseCircle = new mouseBall(undefined,undefined,50,'green')
    for (var i = 0; i < 1; i++) {
        var ranx = random(canvas.width);
        var rany = random(canvas.height)-75;
        var ranradias = random(75);
        var rancolor = 'rgb('+random(255)+', '+random(255)+', '+random(255)+')'
        var ranspeedy = ranrange(20,30)
        var ranspeedx = ranrange(-20,20)
        ballArray.push(new gravityBall(ranx,rany,ranradias,rancolor,ranspeedy,ranspeedx))
    };
    //balls = new gravityBall(300,canvas.height-700,50,'red',10,50)
};


function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0,0,canvas.width,canvas.height);
    for (var i = 0; i < ballArray.length; i++) {
        //getDistance(mouseCircle.x,mouseCircle.y,ballArray[i]);
        ballArray[i].update();
    };
    mouseCircle.update();
    //balls.update();
    //getDistance(mouseCircle.x,mouseCircle.y,balls)
};

init();
animate();

