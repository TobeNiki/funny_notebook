export function socket_InputOutput(input_form,input_text, output){
    var socketio = io();
    $(function(){
        $(input_form).submit(() => {
            if ($(input_text).val() === ''){
                console.log('入力');
            }else{
                socketio.emit(output,$(input_text).val());
                $(input_text).val('');
            }
            return false;
        });
        socketio.on(output,(msg) => {
        $('#'+output).append($('<li>').text(msg));
        });
    });
}