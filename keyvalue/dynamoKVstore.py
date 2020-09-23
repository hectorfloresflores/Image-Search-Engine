import boto3

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.client("dynamodb")


class DynamoDBKeyValue():
    
    def __init__(self,tableName):
        super().__init__()
        print("Tabla a Utilizar: "+tableName)
        self._table = tableName

    def putItem(self,key, Nvalues="{}"):

        dynamodb.put_item(TableName=self._table, Item={"key": {"S": key}, "values": Nvalues})

        return None

    def getItem(self,key,sort="none"):
        req = dynamodb.get_item(TableName=self._table, Key={"key": {"S": key}})
        return req

    def close(self):

        return None