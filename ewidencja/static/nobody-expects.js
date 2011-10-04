$(document).ready(function(){
    $('#nobody-expects').hide();

    $('#id_city').change(function(){
        $('#nobody-expects').toggle();
    });

});