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
            effect: 'none',
        }
    });
    //mic button click event
    $("#MicButton").click(function (e) { 
    eel.playAssistantSound();    
    $("#Oval").attr("Hidden", true);
    $("#SiriWave").attr("Hidden", false);
    eel.allCommands()()        
    });


    function doc_keyUp(e){

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    
    function PLayAssistant(message){

        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicButton").attr("hidden", false);
            $("#SendButton").attr("hidden", true);
            
        }
    }


    function ShowhiddenButtons(message){
        if (message.length == 0){
            $("#MicButton").attr("hidden", false);
            $("#SendButton").attr("hidden", true);
            
        }
        else{
            $("#MicButton").attr("hidden", true);
            $("#SendButton").attr("hidden", false);
            
        }
    }

    $("#chatbox").keyup(function() {

        let message = $("#chatbox").val();
        ShowhiddenButtons(message)
    });

    $("#SendButton").click(function () {

        let message = $("#chatbox").val()
        PLayAssistant(message)
    });

    $("#chatbox").keypress(function (e) {
        key = e.which;
        if(key == 13)  // the enter key code
        {
            let message = $("#chatbox").val()
            PLayAssistant(message)
        }
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
 