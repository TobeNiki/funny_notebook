var socketio = io();
      $(function(){
          $('#code_form').submit(function(){
            if ($('#input_code').val() === ''){
              console.log('入力して');
            }else{
              socketio.emit('code_msg', $('#input_code').val());
              $('#input_code').val('');
            }
            return false;
          });
          socketio.on('code_msg',function(msg){
            $('#code_msg').append($('<li>').text(msg));
        });
    });