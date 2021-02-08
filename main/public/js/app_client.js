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
        })
    });