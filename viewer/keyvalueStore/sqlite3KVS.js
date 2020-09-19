const KVS = require('./kvs')
const sqlite3 = require('sqlite3').verbose()

var SQLite3KVS = function(fileName) { 
    this.db = new sqlite3.Database(fileName, (err) => {
        if (err) {
            console.log(err.message);
        } else {
            console.log("Conectados con Archivo de Base de Datos" + fileName);
        }
    });
}

SQLite3KVS.prototype = Object.create(KVS.prototype);

SQLite3KVS.prototype.getItem = function(key) {
    return new Promise((resolve, reject) => {
        this.db.all("SELECT value FROM KeyValue WHERE key=?", [key], (err, rows) => {
            if(err) {
                console.log("Error runing query")
                console.log(err)
                reject(err)
            } else {
                resolve(rows)
            }
        }) 

    })
}

SQLite3KVS.prototype.close = function() {
    this.db.close(function(err) {
        if(err) {
            console.log(err.message)
        } else {
            console.log("Base de Datos Cerrada")
        }

    });
}

module.exports = SQLite3KVS;



