

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


     // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });


// ---------------- INITIAL LOAD ----------------
eel.personalInfo();
eel.displaySysCommands();
eel.displayWebCommands();
eel.displayContacts();

// Refresh data when settings modal opens
$('#exampleModal').on('show.bs.modal', function () {
    eel.displaySysCommands();
    eel.displayWebCommands();
    eel.displayContacts();
});



// ---------------- PERSONAL INFO ----------------
eel.expose(getData);
function getData(user_info) {
    let data = JSON.parse(user_info);

    let textIds = ['OwnerName', 'Designation', 'MobileNo', 'Email', 'City'];
    let inputIds = ['InputOwnerName', 'InputDesignation', 'InputMobileNo', 'InputEmail', 'InputCity'];

    for (let i = 0; i < data.length; i++) {
        $("#" + textIds[i]).text(data[i]);
        $("#" + inputIds[i]).val(data[i]);
    }
}

$("#UpdateBtn").click(() => {
    let name = $("#InputOwnerName").val();
    let des = $("#InputDesignation").val();
    let mob = $("#InputMobileNo").val();
    let email = $("#InputEmail").val();
    let city = $("#InputCity").val();

    if (name && des && mob && email && city) {
        eel.updatePersonalInfo(name, des, mob, email, city);
        eel.personalInfo();
        swal("Updated Successfully", "", "success");
    }
});


// ---------------- SYSTEM COMMANDS ----------------
eel.expose(displaySysCommands);
function displaySysCommands(array) {
    let data = JSON.parse(array);
    let out = "";
    let i = 1;

    data.forEach(row => {
        out += `
        <tr>
            <td>${i++}</td>
            <td>${row[1]}</td>
            <td>${row[2]}</td>
            <td><button class="btn btn-outline-danger btn-sm delete-sys-btn" data-id="${row[0]}">
                    Delete
                </button>
            </td>
        </tr>`;
    });

    $("#TableData").html(out);
}

$(document).on('click', '.delete-sys-btn', function() {
    let id = $(this).data('id');
    console.log("Deleting sys id:", id);
    eel.deleteSysCommand(id);
    $(this).closest('tr').remove();
    swal("Deleted Successfully", "", "success");
});

$("#SysCommandAddBtn").click(() => {
    eel.addSysCommand($("#SysCommandKey").val(), $("#SysCommandValue").val());
    eel.displaySysCommands();
    $("#SysCommandKey").val("");
    $("#SysCommandValue").val("");
    swal("Added Successfully", "", "success");
});


// ---------------- WEB COMMANDS ----------------
eel.expose(displayWebCommands);
function displayWebCommands(array) {
    let data = JSON.parse(array);
    let out = "";
    let i = 1;

    data.forEach(row => {
        out += `
        <tr>
            <td>${i++}</td>
            <td>${row[1]}</td>
            <td>${row[2]}</td>
            <td><button class="btn btn-outline-danger btn-sm delete-web-btn" data-id="${row[0]}">
                    Delete
                </button></td>
        </tr>`;
    });

    $("#WebTableData").html(out);
}

$(document).on('click', '.delete-web-btn', function() {
    let id = $(this).data('id');
    console.log("Deleting web id:", id);
    eel.deleteWebCommand(id);
    $(this).closest('tr').remove();
    swal("Deleted Successfully", "", "success");
});



$("#WebCommandAddBtn").click(() => {
    eel.addWebCommand($("#WebCommandKey").val(), $("#WebCommandValue").val());
    eel.displayWebCommands();
    $("#WebCommandKey").val("");
    $("#WebCommandValue").val("");
    swal("Added Successfully", "", "success");
});


// ---------------- CONTACTS ----------------
eel.expose(displayContacts);
function displayContacts(array) {
    let data = JSON.parse(array);
    let out = "";
    let i = 1;

    data.forEach(row => {
        out += `
        <tr>
            <td>${i++}</td>
            <td>${row[1]}</td>
            <td>${row[2]}</td>
            <td>${row[3]}</td>
            <td>${row[4]}</td>
            <td><button class="btn btn-outline-danger btn-sm delete-contact-btn" data-id="${row[0]}">
                    Delete
                </button></td>
        </tr>`;
    });

    $("#ContactTableData").html(out);
}

$(document).on('click', '.delete-contact-btn', function() {
    let id = $(this).data('id');
    console.log("Deleting contact id:", id);
    eel.deleteContact(id);
    $(this).closest('tr').remove();
    swal("Deleted Successfully", "", "success");
});



$("#AddContactBtn").click(() => {
    eel.addContact(
        $("#InputContactName").val(),
        $("#InputContactMobileNo").val(),
        $("#InputContactEmail").val(),
        $("#InputContactCity").val()
    );
    eel.displayContacts();
    $("#InputContactName").val("");
    $("#InputContactMobileNo").val("");
    $("#InputContactEmail").val("");
    $("#InputContactCity").val("");
    swal("Added Successfully", "", "success");
});
});


