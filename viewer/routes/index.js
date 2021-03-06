var express = require('express');
var stemmer = require('porter-stemmer').stemmer;

//var KVS = require('../keyvalueStore/sqlite3KVS');
var KVS = require('../keyvalueStore/dynamoKVS');

var router = express.Router();

var kvs_labels = new KVS('../labels.db')  //@Update to match DynamoDB
var kvs_images = new KVS('../images.db')  //@Update to match DynamoDB

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/search/:word', async function(req, res, next) {
  imagesUrls = new Array();
  steamWord = stemmer(req.params.word.toLowerCase());
  list_words = steamWord.split(' ')
    list_urls = new Array()
    console.log(list_words)
    final_list = []

  for (let i = 0; i < list_words.length; i++) {

      list_urls.push(KVS.prototype.getItem(list_words[i], "labels"));
      //list_urls.push(kvs_labels.getItem(list_words[i]));
  }
  Promise.all(list_urls).then(items=>{
      console.log(items)

        for (let j = 0; j < items.length; j++) {
            for (let k = 0; k < items[j].length; k++) {
                imagesUrls.push(KVS.prototype.getItem(items[j][k], "images"));
            }
        }


      Promise.all(imagesUrls).then(result => {
          console.log(result)

           for (let k = 0; k < result.length; k++) {
               final_list.push(result[k]);
           }

           //console.log(final_list)
        console.log("Regresando "+final_list.length+" URLs")
        res.send(JSON.stringify({results: final_list, num_results: final_list.length}))
      }).catch(error =>{
        res.send(`Error in promises ${error}`)
      })
  })
});

module.exports = router;
