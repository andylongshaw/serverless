import unittest
import uuid
import json
import boto3
import time


class CustomerIntegrationTests(unittest.TestCase):



    def test_raw_create_and_retrieve(self):
        customer_id = 'A1234'
        customer_name = 'Fred Bloggs'
        table_name = 'SPA' + str(uuid.uuid4())

        dynamo_proxy = DynamoProxy(table_name)

        dynamo_proxy.create_customer_record(customer_id, customer_name)

        response = dynamo_proxy.retrieve_customer_record(customer_id)

        self.assertTrue('Item' in response, 'No item returned from get_item')

        item = response['Item']

        self.assertEqual(customer_id, item['customerId'])

        dynamo_proxy.close()


class DynamoProxy():

    def __init__(self, table_name):
        dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')

        self.table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'customerId',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'customerId',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        self.table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

        print("Table created" + str(self.table))

    def close(self):
        if self.table is not None:
            print('Deleting table ' + str(self.table))
            self.table.delete()

    def create_customer_record(self, customer_id, customer_name):
        self.table.put_item(
            Item={
                'customerId': customer_id,
                'name': customer_name
            }
        )

    def retrieve_customer_record(self, customer_id):
        response = self.table.get_item(
            Key={
                'customerId': customer_id
            }
        )
        return response


if __name__ == '__main__':
    unittest.main()
