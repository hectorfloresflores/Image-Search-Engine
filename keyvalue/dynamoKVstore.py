import boto3

import boto3
dynamodb = boto3.client("dynamodb")

print(dynamodb.put_item(TableName='labels',  Item={"key":{"SS":["1","2"]}}))
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('labels')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

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