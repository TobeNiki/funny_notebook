const express = require('express');
const app = express();
const helmet = require('helmet');
const http = require('http').Server(app);
const PORT = process.env.PORT || 3000;
const io = require('socket.io')(http);

//const mongo = require('mongodb');
//const { title } = require('process');
//const DBClient = mongo.MongoClient;

const apiclient = require('./code_post.js');
const dbclient = require('./model.js');
app.set('view engine', 'ejs');
app.use(express.static('public'));
/* 
jquery,bootstrap等のライブラリはpublic/libraryに
min.js,min.js.mapファイルを置く形で利用(gitignoreで追跡対象外に指定)
*/
app.use(helmet());

app.get('/', (req, res) => {
    var titles = "Funny Notebook";
    res.render('app',{title:titles});
});

app.get('/chat', (req, res) => {
    var titles = "Funny Chats";
    res.render('chat',{title:titles});
});

io.on('connection', (socket) => {
    socket.on('code_msg',(msg) => {
        apiclient.code_post(msg).then((response) =>{
            result_msg = response.result;
            io.emit('code_msg', result_msg);
            dbclient.insert('test',result_msg);
        });
        //io.emit('message', msg);
    });
    socket.on('text_msg', (msg) => {
        apiclient.text_post(msg).then((response) =>{
            result_msg = response.result;
            console.log("title"+result_msg);
            io.emit('text_msg',result_msg);
            dbclient.insert('test',result_msg);
        })
    })
});

http.listen(PORT, ()=>{
    console.log('server listening. PORT:', + PORT);
});

process.on('exit', ()=>{ 
    dbclient.database_closing();
});