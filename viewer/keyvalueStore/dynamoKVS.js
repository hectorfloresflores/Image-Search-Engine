const KVS = require('./kvs')

var aws = require('aws-sdk');
aws.config.update({
  region: "us-east-1"

});

var db = new aws.DynamoDB();

var docClient = new aws.DynamoDB.DocumentClient();


var params = {
    TableName: 'labels',
    Key:{
        "key": 'dog'
    },

};


var DynammoKVS = function(tableName) {
    //@TODO
    this.db = null
}

DynammoKVS.prototype = Object.create(KVS.prototype);

DynammoKVS.prototype.getItem = function(key, table) {
    return new Promise((resolve, reject) => {
                docClient.get(
                    {
            TableName: table,
            Key:{
                "key": key
            },}
            , function(err, data) {
        if (err) {
            reject(err);
            console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
        } else {

            console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
            resolve(data.Item.values);
        }
        });
    })
}

DynammoKVS.prototype.putItem = function(key) {
    return new Promise((resolve, reject) => {
        //@TODO
    })
}

DynammoKVS.prototype.close = function() {
    //@TODO
}

module.exports = DynammoKVS;



