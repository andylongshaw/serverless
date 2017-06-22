# Extension 1 - invoke the microservice lambda from the API gateway console

1. insert a row in a DynamoDB database table (\<MyAnimal\>Customer) in response to a REST message

1. retrieve a row from a DynamoDB database table (\<MyAnimal\>Customer) in response to a REST message

# Extension 2 - invoke the microservice lambda from the AWS CLI

Python 3 installed locally
sudo pip3 install boto3
sudo pip3 install requests


OR


1. Install the AWS CLI on your laptop following [these instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
1.  Take care to use the configuration file advice on the http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html page, not the regular CLI instructions

use the CLI API
