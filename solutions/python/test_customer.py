import unittest
import uuid
import json
import boto3
import time


class CustomerIntegrationTests(unittest.TestCase):

    def create_table(self, dynamodb, table_name):

        return dynamodb.Table('MyTable')

        table = dynamodb.create_table(
            TableName = table_name,
            KeySchema = [
                {
                    'AttributeName': 'CustomerId',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'Name',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'CustomerId',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Name',
                    'AttributeType': 'S'
                },

            ]
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='users')

        while table.table_status is not 'ACTIVE':
            print("Table not ready. It is still {}. Sleeping for 10 seconds...".format(table.table_status))
            time.sleep(10)

        return table


    def test_create_and_retrieve(self):
        customer_id = 'A1234'
        customer_name = 'Fred Bloggs'
        table_name = 'SPA' + str(uuid.uuid4())

        dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')

        table = self.create_table(dynamodb, table_name)

        table.put_item(
            Item = {
                'CustomerId': customer_id,
                'Name': customer_name
            }
        )

        response = table.get_item(
            Key={
                'CustomerId': 'A1234'
            }
        )

        self.assertTrue('Item' in response, 'No item returned from get_item')

        item = response['Item']

        self.assertEqual(customer_id, item['CustomerId'])


if __name__ == '__main__':
    unittest.main()
