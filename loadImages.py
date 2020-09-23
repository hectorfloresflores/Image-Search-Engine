
from triples import ParseTriples, Triple
import keyvalue.sqliteKVStore as sqliteKVS
import keyvalue.dynamoKVstore as sqliteDyna
import stemmer as s


from urllib.parse import urlparse
from os.path import splitext, basename

imagesStore = sqliteKVS.SqliteKeyValue("images.db")
termsStore = sqliteKVS.SqliteKeyValue("labels.db")

imagesDS = ParseTriples("images.ttl")
labelsDS = ParseTriples("labels_en.ttl")

predicate = 'http://xmlns.com/foaf/0.1/depiction'


labelsDyna = sqliteDyna.DynamoDBKeyValue("labels")
imagsDyna = sqliteDyna.DynamoDBKeyValue("images")

#Uncoment but just run once to load all images possibles
#Ejemplo de uso del Parser.
image = imagesDS.getNext()
couner = 0

dictionary = {}
dictionaryLabels = {}




for i in range(0, 5000):

    disassembled = urlparse(image.getObject())
    filename, file_ext = splitext(basename(disassembled.path))
    file_ext = str(file_ext).lower()
    if predicate == image.getPredicate() and (file_ext == '.jpg' or file_ext == '.png'):
        #imagesStore.putItem(image.getSubject(), value=image.getObject())
        if image.getSubject() not in dictionary:
            dictionary[image.getSubject()] = image.getObject()


        print(image.getSubject() + " -- " + image.getObject())

    image = imagesDS.getNext()
#
# for key, value in dictionary.items():
#     h = 0
#     imagsDyna.putItem(key, {"S" :value})

for i in range(0, 5000):

    label = labelsDS.getNext()

    #if len(labelsDyna.getItem(label.getSubject())) > 0:
    stemmer = s.stem(label.getObject())
    #Note that label could have mutiple values so iterate thorough the list
    for word in stemmer.split(" "):
        if label.getSubject() in dictionary:
            if word in dictionaryLabels:
                dictionaryLabels[word].append({"S": label.getSubject()})
            else:
                dictionaryLabels[word] = [{"S": label.getSubject()}]
            print(word + " is asociated with "+label.getObject()+" " +label.getSubject())
        #termsStore.putItem(key=word, value=label.getSubject())

for key, value in dictionaryLabels.items():
    h = 0
    labelsDyna.putItem(key, {"L": value})


imagesStore.close()
termsStore.close()






