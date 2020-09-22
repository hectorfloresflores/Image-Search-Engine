
from triples import ParseTriples, Triple
import keyvalue.sqliteKVStore as sqliteKVS
import stemmer as s
from urllib.parse import urlparse
from os.path import splitext, basename

imagesStore = sqliteKVS.SqliteKeyValue("images.db")
termsStore = sqliteKVS.SqliteKeyValue("labels.db")

imagesDS = ParseTriples("images.ttl")
labelsDS = ParseTriples("labels_en.ttl")

predicate = 'http://xmlns.com/foaf/0.1/depiction'

#Uncoment but just run once to load all images possibles
#Ejemplo de uso del Parser.
# image = imagesDS.getNext()
# couner = 0
# while image:
#
#     disassembled = urlparse(image.getObject())
#     filename, file_ext = splitext(basename(disassembled.path))
#     file_ext = str(file_ext).lower()
#     if predicate == image.getPredicate() and (file_ext == '.jpg' or file_ext == '.png'):
#         imagesStore.putItem(image.getSubject(), value=image.getObject())
#
#     image = imagesDS.getNext()
#
#     print(couner)
#     couner = couner + 1


for i in range(0, 5000):

    label = labelsDS.getNext()

    if len(imagesStore.getItem(label.getSubject())) > 0:
        stemmer = s.stem(label.getObject())
        #Note that label could have mutiple values so iterate thorough the list
        for word in stemmer.split(" "):
            print(word + " is asociated with "+label.getObject()+" " +label.getSubject())
            termsStore.putItem(key=word, sort=i, value=label.getSubject())
            print()



imagesStore.close()
termsStore.close()






