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


    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
                <div class = "width-size">
                <div class="sender_message">${message}</div>
                </div>
                </div>`;
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
                <div class = "width-size">
                <div class="receiver_message">${message}</div>
                </div>
                </div>`;
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    }
});
