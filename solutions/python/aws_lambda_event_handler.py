import boto3
import json
import uuid

# print('Loading function')
dynamo = boto3.resource("dynamodb", region_name='eu-west-1')
table_name = 'Bat-PendingEmailTable'


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    for recordInfo in event['Records']:
        record = recordInfo['dynamodb']['NewImage']
        create_email_record(record['customerId']['S'], record['name']['S'])


def create_email_record(customer_id, customer_name):
    table = dynamo.Table(table_name)
    email_id = "{}_{}".format(customer_id, str(uuid.uuid4()))
    response = table.put_item(
        Item={
            'emailId': email_id,
            'name': customer_name
        }
    )
    return response
