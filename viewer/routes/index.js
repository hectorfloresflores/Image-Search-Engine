var express = require('express');
var stemmer = require('porter-stemmer').stemmer;

var KVS = require('../keyvalueStore/sqlite3KVS');
//var KVS = require('../keyvalueStore/dynamoKVS');

var router = express.Router();

var kvs_labels = new KVS('../labels.db')  //@Update to match DynamoDB
var kvs_images = new KVS('../images.db')  //@Update to match DynamoDB

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/search/:word', async function(req, res, next) {
  var imagesUrls = new Array();        

  steamWord = stemmer(req.params.word.toLowerCase());    
  await kvs_labels.getItem(steamWord).then(function(items) { 
    //@TODO cada item de items que nos regrese debemos buscar 
    // su URL y agregarla al arreglo imagesURLs. 
    
    //Dado que el metodo getItem del KVS es asyncrono se recomida 
    //recuperar el promise de cada consulta y agregarla a un arreglo
    //para al final esperar que terminen todos con la función
    //await Promise.all(arreglo_de_promises)
    
  }).catch((e) => {
    //Cuando el promise falla se manda llamar esta función.
    res.send(JSON.stringify({results: [], num_results: 0, error: e}))
  })
 
  console.log("Regresando "+imagesUrls.length+" URLs")
  res.send(JSON.stringify({results: imagesUrls, num_results: imagesUrls.length}))
});

module.exports = router;
