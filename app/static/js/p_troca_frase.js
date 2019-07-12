$(document).ready(function(){
    let frases = ['Incrível', 'Forte', 'Poderosa', 'Confiante', 'Empoderada', 'Resistência' ];
    let cont = 0;

    $('#troca').text(frases[cont++]);
    setInterval(function(){
        $('#troca').fadeOut(function(){
            if (cont >= frases.length) cont = 0;
            $('#troca').text(frases[cont++]).fadeIn();
        });
    }, 3000);
});