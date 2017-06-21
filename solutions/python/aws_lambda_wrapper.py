import boto3
import json

print('Loading function')
dynamo = boto3.resource("dynamodb", region_name='eu-west-1')
table_name='ZebraCustomer'


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))

    method = event['httpMethod']

    if method == 'GET':
        body = event['body']
        response = retrieve_customer_record(body['customerId'])
        err = None
    elif method == 'POST':
        body = event['body']
        response = create_customer_record(body['customerId'], body['name'])
        err = None
    else:
        err = ValueError('Unsupported method "{}"'.format(method))
        response = None

    return respond(err, response)


def create_customer_record(customer_id, customer_name):
    table = dynamo.Table(table_name)
    response = table.put_item(
        Item={
            'customerId': customer_id,
            'name': customer_name
        }
    )
    return response


def retrieve_customer_record(customer_id):
    table = dynamo.Table(table_name)
    response = table.get_item(
        Key={
            'customerId': customer_id
        }
    )
    return response
