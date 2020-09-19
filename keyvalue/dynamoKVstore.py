import boto3

class DynamoDBKeyValue():
    
    def __init__(self,tableName):
        super().__init__()
        print("Tabla a Utilizar: "+tableName)
        self._table = tableName

    def putItem(self,key,sort="none",value="{}"):
        return None

    def getItem(self,key,sort="none"):
        return ("{}",)

    def close(self):
        return None