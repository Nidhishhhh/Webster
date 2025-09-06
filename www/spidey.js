window.addEventListener("load", windowLoadHandler, false);

document.addEventListener('mousemove', function(event) {
    // Access mouse coordinates:
    const mouseX = event.clientX; // X-coordinate relative to the viewport
    const mouseY = event.clientY; // Y-coordinate relative to the viewport

    // Or relative to a specific element:
    // const element = document.getElementById('myElement');
    // const elementRect = element.getBoundingClientRect();
    // const relativeX = event.clientX - elementRect.left;
    // const relativeY = event.clientY - elementRect.top;

    // Implement your reactive effect here
});

const follower = document.getElementById('mouse-follower');

document.addEventListener('mousemove', function(event) {
    follower.style.left = (event.clientX - follower.offsetWidth / 2) + 'px';
    follower.style.top = (event.clientY - follower.offsetHeight / 2) + 'px';
});

var sphereRad = 140;
var radius_sp = 1;

function windowLoadHandler() {
    canvasApp();
}

function canvasSupport() {
    return !!document.createElement('canvas').getContext;
}

function canvasApp() {
    if (!canvasSupport()) {
        return;
    }

    var theCanvas = document.getElementById("canvasOne");
    var context = theCanvas.getContext("2d");

    var displayWidth = theCanvas.width;
    var displayHeight = theCanvas.height;
    var particleList = [];
    var particleAlpha = 1;
    var fLen = 320;
    var projCenterX = displayWidth / 2;
    var projCenterY = displayHeight / 2;
    var zMax = fLen - 2;
    var turnSpeed = 2 * Math.PI / 1200; // Controls spin speed
    var turnAngle = 0;
    var sphereCenterZ = 0; // Center Z at origin for on-the-spot spin
    var gravity = -0.1;
    var particleRad = 1.0;
    var rgbString = "rgba(255, 255, 255, ";

    function init() {
        setInterval(onTimer, 1000 / 60); // 60 FPS
    }

    function onTimer() {
        turnAngle = (turnAngle + turnSpeed) % (2 * Math.PI);
        var sinAngle = Math.sin(turnAngle);
        var cosAngle = Math.cos(turnAngle);

        context.fillStyle = "#000000";
        context.fillRect(0, 0, displayWidth, displayHeight);

        // Add new particles
        if (particleList.length < 100) {
            var theta = Math.random() * 2 * Math.PI;
            var phi = Math.acos(Math.random() * 2 - 1);
            var x0 = sphereRad * Math.sin(phi) * Math.cos(theta);
            var y0 = sphereRad * Math.sin(phi) * Math.sin(theta);
            var z0 = sphereRad * Math.cos(phi);
            particleList.push({
                x: x0,
                y: y0,
                z: z0,
                velX: 0.002 * x0,
                velY: 0.002 * y0,
                velZ: 0.002 * z0,
                age: 0,
                alpha: 0,
                attack: 50,
                hold: 50,
                decay: 100
            });
        }

        // Update and draw particles
        var activeParticles = [];
        for (var i = 0; i < particleList.length; i++) {
            var p = particleList[i];
            p.age++;

            if (p.age > 90) {
                p.velX += (Math.random() * 0.2 - 0.1);
                p.velY += gravity + (Math.random() * 0.2 - 0.1);
                p.velZ += (Math.random() * 0.2 - 0.1);
                p.x += p.velX;
                p.y += p.velY;
                p.z += p.velZ;

                // Constrain particles within sphere radius
                var dist = Math.sqrt(p.x * p.x + p.y * p.y + p.z * p.z);
                if (dist > sphereRad) {
                    p.x = (p.x / dist) * sphereRad;
                    p.y = (p.y / dist) * sphereRad;
                    p.z = (p.z / dist) * sphereRad;
                    p.velX *= 0.9;
                    p.velY *= 0.9;
                    p.velZ *= 0.9;
                }

            }

            // Rotate particles around their own center
            var rotX = cosAngle * p.x - sinAngle * p.y;
            var rotY = sinAngle * p.x + cosAngle * p.y;
            var rotZ = p.z; // Keep Z rotation minimal for on-the-spot effect

            var m = radius_sp * fLen / (fLen - rotZ);
            p.projX = rotX * m + projCenterX;
            p.projY = rotY * m + projCenterY;

            if (p.age < p.attack + p.hold + p.decay) {
                if (p.age < p.attack) {
                    p.alpha = (particleAlpha / p.attack) * p.age;
                } else if (p.age < p.attack + p.hold) {
                    p.alpha = particleAlpha;
                } else {
                    p.alpha = particleAlpha * (1 - (p.age - p.attack - p.hold) / p.decay);
                }
            } else {
                p.alpha = 0;
            }

            if (p.projX > 0 && p.projX < displayWidth && p.projY > 0 && p.projY < displayHeight && rotZ < zMax && p.alpha > 0) {
                activeParticles.push(p);
            }
        }

        // Draw web connections
        context.strokeStyle = rgbString + "0.5)";
        context.lineWidth = 0.5;
        for (var i = 0; i < activeParticles.length; i++) {
            for (var j = i + 1; j < activeParticles.length; j++) {
                var p1 = activeParticles[i];
                var p2 = activeParticles[j];
                var dx = p1.projX - p2.projX;
                var dy = p1.projY - p2.projY;
                var dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 50) {
                    context.beginPath();
                    context.moveTo(p1.projX, p1.projY);
                    context.lineTo(p2.projX, p2.projY);
                    context.stroke();
                }
            }
        }

        // Draw particles
        context.fillStyle = rgbString + "1)";
        for (var i = 0; i < activeParticles.length; i++) {
            var p = activeParticles[i];
            var depthAlphaFactor = (1 - p.z / -750);
            depthAlphaFactor = Math.max(0, Math.min(1, depthAlphaFactor));
            context.fillStyle = rgbString + (depthAlphaFactor * p.alpha) + ")";
            context.beginPath();
            context.arc(p.projX, p.projY, m * particleRad, 0, 2 * Math.PI, false);
            context.closePath();
            context.fill();
        }

        // Clean up dead particles
        particleList = particleList.filter(p => p.alpha > 0);
    }

    // Slider updates
    $("#slider-range").slider({
        range: false,
        min: 20,
        max: 200,
        value: 140,
        slide: function (event, ui) {
            sphereRad = ui.value;
        }
    });

    $("#slider-test").slider({
        range: false,
        min: 1.0,
        max: 2.0,
        value: 1,
        step: 0.01,
        slide: function (event, ui) {
            radius_sp = ui.value;
        }
    });

    init();
}