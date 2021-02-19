const express = require('express');
const app = express();
const helmet = require('helmet');
const http = require('http').Server(app);
const PORT = process.env.PORT || 3000;
const io = require('socket.io')(http);

const mongo = require('mongodb');
//const { title } = require('process');
const DBClient = mongo.MongoClient;

const apiclient = require('./code_post.js')

app.set('view engine', 'ejs');
app.use(express.static('public'));
/* 
jquery,bootstrap等のライブラリはpublic/libraryに
min.js,min.js.mapファイルを置く形で利用(gitignoreで追跡対象外に指定)
*/
app.use(helmet());

app.get('/', function(req, res){
    var titles = "Funny Notebook";
    res.render('app',{title:titles});
});

app.get('/chat', function(req, res){
    var titles = "Funny Chats";
    res.render('chat',{title:titles});
});

io.on('connection',function(socket){
    socket.on('code_msg',function(msg){
        apiclient.code_post(msg).then((response) =>{
            titles = response.result;
            io.emit('code_msg', titles);
        });
        //io.emit('message', msg);
    });
    socket.on('text_msg',function(msg){
        apiclient.text_post(msg).then((response) =>{
            titles = response.result;
            console.log("title"+titles)
            io.emit('text_msg',titles);
        })
    })
});

http.listen(PORT, function(){
    console.log('server listening. PORT:', + PORT);
});