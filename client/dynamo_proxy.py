import boto3
from botocore.client import ClientError

class DynamoProxy():

    def __init__(self, table_name):
        self.table_name = table_name
        self.ddb_client = boto3.client("dynamodb")
        self.ddb_resource = boto3.resource("dynamodb", region_name='eu-west-1')

        try:
            self.ddb_client.describe_table(TableName=table_name)
            self.table_already_existed = True
            print('Table {} already exists'.format(table_name))
        except ClientError as e:
            print('Table {} does not appear to exist, creating...'.format(table_name))
            self.table_already_existed = False
            table = self.ddb_resource.create_table(
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

            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

            print('Table created {}'.format(str(table)))

    def close(self):
        if self.table_already_existed is False:
            print('Deleting table {}'.format(self.table_name))
            table = self.ddb_resource.Table(self.table_name)
            table.delete()

    def create_customer_record(self, customer_id, customer_name):
        table = self.ddb_resource.Table(self.table_name)
        table.put_item(
            Item={
                'customerId': customer_id,
                'name': customer_name
            }
        )

    def retrieve_customer_record(self, customer_id):
        table = self.ddb_resource.Table(self.table_name)
        response = table.get_item(
            Key={
                'customerId': customer_id
            }
        )
        return response

