const KVS = require('./kvs')

var DynammoKVS = function(tableName) { 
    //@TODO
    this.db = null
}

DynammoKVS.prototype = Object.create(KVS.prototype);

DynammoKVS.prototype.getItem = function(key) {
    return new Promise((resolve, reject) => {
        //@TODO
    })
}

DynammoKVS.prototype.close = function() {
    //@TODO
}

module.exports = DynammoKVS;



