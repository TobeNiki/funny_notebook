const express = require('express');
const app = express();

const http = require('http').Server(app);
const PORT = process.env.PORT || 3000;

const io = require('socket.io')(http);

const mongo = require('mongodb');
const DBClient = mongo.MongoClient;

const apiclient = require('./code_post.js')

app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', function(req, res){
    var titles = "Funny Notebook";
    res.render('app',{title:titles});
});
io.on('connection',function(socket){
    socket.on('message',function(msg){
        apiclient.code_post(msg).then((response) =>{
            titles = response.result
            io.emit('message', titles);
        });
        //io.emit('message', msg);
    });
});

http.listen(PORT, function(){
    console.log('server listening. PORT:', + PORT);
});