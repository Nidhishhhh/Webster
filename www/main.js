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
    //siri config
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: 'ios9',
    amplitude: 1,
    speed: 0.20,
    autostart: true
  });

  $('.siri-message').textillate({
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
   

});






// Set styles for the SiriWave container
//var siriContainer = document.getElementById("siri-container");
//siriContainer.style.position = 'absolute';
//siriContainer.style.top = '50%';  
//siriContainer.style.left = '50%'; 
//iriContainer.style.transform = 'translate(-50%, -50%)'; 


//siri message animation

    //mic button click event
 