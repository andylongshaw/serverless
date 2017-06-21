import boto3
import json

print('Loading function')
dynamo = boto3.resource("dynamodb", region_name='eu-west-1')
table_name = 'ZebraPendingEmails'


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        create_email_record(record('eventID'), record['name'])


def create_email_record(email_id, customer_name):
    table = dynamo.Table(table_name)
    response = table.put_item(
        Item={
            'emailId': email_id,
            'name': customer_name
        }
    )
    return response
