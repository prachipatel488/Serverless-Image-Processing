import json
import boto3
import uuid

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # TODO implement
    
    bucket = "wildrydes-step-module-resource-riderphotos3bucket-18xyzcvph91xl"
    image = event[u'ObjectID']
    userId = event[u'UserName']
    
    ID =  str(uuid.uuid1())
    
    input = {'userId': userId, 's3Bucket': bucket, 's3Key': image}
    
    response = client.start_execution(
        stateMachineArn='arn:aws:states:us-east-1:994030152439:stateMachine:MyStateMachine',
        name=ID,
        input=json.dumps(input)
        )
    
    print(event)
    
    return "Hello from lambda"