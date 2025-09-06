$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeIn',
        },
        out: {
            effect: 'fadeOut',
        }
    });    
});

$('.siri-message').textillate({
        loop: true,
        in: {
            effect: 'fadeInUp',
            sync: false
        },
        out: {
            effect: 'fadeOutUp',
            sync: false
        }
    });

//Siri Config
var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: 'ios9',
    amplitude: 1,
    speed: 0.20,
    autostart: true
  });

 