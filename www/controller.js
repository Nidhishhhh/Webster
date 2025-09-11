//Display Speak Message
$(document).ready(function () {
        eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    }
    
    //Display Hood after the Webster answers your question
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("Hidden", false);
        $("#SiriWave").attr("Hidden", true);
        DelayNode(3000).then(() => {
            $("#Oval").attr("Hidden", true);
        });
    }
});
