const request = require('request-promise');

exports.code_post = function (code){
    var options = {
        uri:"http://127.0.0.1:8000/bf_compiler",
        method:"POST",
        headers:{
            'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        },
        body:{"bf": code},
        json:true,
    };
    return new Promise((resolve,reject) => {request(options)
        .then((response) => {
            resolve(response);
        })
        .catch((error) => {
            reject(error);
        });
    });
};