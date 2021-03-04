const request = require('request-promise');

var options = {
    uri:"",
    method:"POST",
    headers:{
        'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    },
    body:{},
    json:true,
};

exports.code_post = function (code){
    options.uri = "http://127.0.0.1:8000/bf_compiler";
    options.body = {"bf":code};
    return new Promise((resolve,reject) => {request(options)
        .then((response) => {
            resolve(response);
        })
        .catch((error) => {
            reject(error);
        });
    });
};

exports.text_post = function (text){
    options.uri = "http://127.0.0.1:8000/text_to_bfcode";
    options.body = {"text":text};
    return new Promise((resolve,reject) => {request(options)
        .then((response) =>{
            console.log(response);
            resolve(response);
        })
        .catch((error) => {
            console.log(error);
            reject(error);
        });
    });
};