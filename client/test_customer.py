import unittest
import uuid
import requests
from dynamo_proxy import DynamoProxy


class CustomerIntegrationTests(unittest.TestCase):

    def test_microservice_create_and_retrieve(self):
        #table_name = 'SPA' + str(uuid.uuid4())
        table_name = 'ZebraTable'

        dynamo_proxy = DynamoProxy(table_name)

        with open('../../messages/DynamoDB_microservice_message_insert.json', 'r') as myfile:
            insert_message = myfile.read().replace('\n', '')

        print(insert_message)

        url = 'https://opf5rml8y5.execute-api.eu-west-1.amazonaws.com/prod/DynamoFunction'

        response = requests.post(url, data=insert_message)

        print(response)

        dynamo_proxy.close()


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


if __name__ == '__main__':
    unittest.main()
