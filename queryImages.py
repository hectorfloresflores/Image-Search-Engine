import sys

from triples import ParseTriples, Triple
import keyvalue.sqliteKVStore as sqliteKVS
import stemmer as s


imagesStore = sqliteKVS.SqliteKeyValue("images.db")
labelsStore = sqliteKVS.SqliteKeyValue("labels.db")

if(len(sys.argv) < 2):
    print("Es necesario indicar la o las palabras a buscar Ejemplo:")
    print("{0} palabra1".format(sys.argv[0]))

for word in sys.argv[1:]:
    w = s.stem(word)

    newword = labelsStore.getItem(w)

    print(newword)
    #if len(word) > 0:
    #    print(imagesStore.getItem(word[0][0]))
    #@TODO Aqui debemos programar la logica de buscar las URLs
    #asociadas a cada palabra que nos den via la linea de comandos.
    

imagesStore.close()
labelsStore.close()