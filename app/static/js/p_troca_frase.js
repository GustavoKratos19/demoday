$(document).ready(function(){
    let frases = ['incrível', 'forte', 'poderosa', 'confiante', 'empoderada', 'resistência' ];
    let cont = 0;

    $('#troca').text(frases[cont++]);
    setInterval(function(){
        $('#troca').fadeOut(function(){
            if (cont >= frases.length) cont = 0;
            $('#troca').text(frases[cont++]).fadeIn();
        });
    }, 3000);
});