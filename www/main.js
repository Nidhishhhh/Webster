$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeIn',
            delayScale: 1.5,
        },
        out: {
            effect: 'fadeOut',
            delayScale: 1.5,
        }
    });    
});