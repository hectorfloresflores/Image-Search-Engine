from triples import ParseTriples, Triple
import keyvalue.sqliteKVStore as sqliteKVS
import stemmer as s

imagesStore = sqliteKVS.SqliteKeyValue("images.db")
termsStore = sqliteKVS.SqliteKeyValue("labels.db")

#Ejemplo de uso del Parser.
#imagesDS = ParseTriples("PathToFile")
#triple = images.getNext()


imagesStore.close()
labelsStore.close()






