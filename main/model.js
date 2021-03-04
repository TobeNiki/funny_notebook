
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('logDatabase.sqlite');
var Puid = require('puid');
var puid = new Puid();

require('date-utils');
let date = new Date();

exports.insert = function (user, msg){
  var now = date.toFormat('YYYY/MM/DD HH24:MI:SS');
  var id = puid.generate();
  return new Promise((resolve, reject) => {
    try{
      db.serialize(()=>{
        var stmt = db.prepare('insert into log values(?, ?, ?, ?)');
        stmt.run([id,user,msg,now]);
        stmt.finalize();
      });
      return resolve();
    }catch(err){
      return reject(err);
    };
  });
};

exports.serect_all = function (col, target){
  return new Promise((resolve, reject) => {
    db.serialize(() => {
      db.all(`select id, user, message from log where ${col}=${target};`,
      (err, row) => {
        if (err) return reject(err);
        return resolve(row);
      });
    });
  });
};

exports.serect_one = function (col, target){
  return new Promise((resolve, reject) => {
    db.serialize(() => {
      db.each(`select id, user, message from log where ${col}=${target};`,
      (err, row) => {
        if (err) return reject(err);
        return resolve(row);
      });
    });
  });
};

exports.database_closing = function(){
  db.close();
};