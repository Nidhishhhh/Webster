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

// Set styles for the SiriWave container
var siriContainer = document.getElementById("siri-container");
siriContainer.style.position = 'absolute';
siriContainer.style.top = '50%';  // Vertically center
siriContainer.style.left = '50%'; // Horizontally center
siriContainer.style.transform = 'translate(-50%, -50%)'; // Offset by half its size to truly center


//siri message animation
$('.text').textillate({
    loop: true,
    sync: true,
    in: {
        effect: 'fadeInUp',
    },
    out: {
        effect: 'fadeOutUp',
    }
});
    //mic button click event
$("#MicButton").click(function (e) { 
    eel.playAssistantSound();    
    $("#Oval").attr("Hidden", true);
    $("#SiriWave").attr("Hidden", false);
        
});
    