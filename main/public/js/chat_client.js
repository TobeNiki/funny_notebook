var socketio = io();
$(function(){
    $('#text_form').submit(function(){
        if ($('#input_text').val() === ''){
            console.log('入力');
        }else{
            socketio.emit('text_msg',$('#input_text').val());
            $('#input_text').val('');
        }
        return false;
    });
    socketio.on('text_msg',function(msg){
    $('#text_msg').append($('<li>').text(msg));
    });
});