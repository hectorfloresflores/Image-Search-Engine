import sqlite3

class SqliteKeyValue():
    
    def __init__(self,dbFile,tableName='KeyValue'):
        super().__init__()
        print("Archivo de BaseDeDatos: "+dbFile)
        self._table = tableName
        self._con = sqlite3.connect(dbFile,timeout=10)
        self._cur = self._con.cursor()
        self._cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name=?', (self._table,))
        if self._cur.fetchone() is None:
                self._cur.execute('CREATE TABLE {0} (key TEXT NOT NULL, sort TEXT NOT NULL, value TEXT,  PRIMARY KEY(key,sort))'.format(self._table))

    def putItem(self,key,sort="none",value="{}"):

        self._cur.execute('INSERT OR REPLACE INTO {0} VALUES (?,?,?)'.format(self._table), (key, sort, value))

    def getItem(self,key,sort="none"):
        if(sort == "none"):
            self._cur.execute('SELECT value FROM {0} WHERE key=?'.format(self._table), (key,))
        else:
            self._cur.execute('SELECT value FROM  {0} WHERE key=? AND sort =?'.format(self._table), (key,sort))
        
        row = self._cur.fetchall()
        if row is None:
           return None
        return row

    def close(self):
        self._con.commit()
        self._con.close()