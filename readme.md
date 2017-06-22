# Objective
To create two AWS lambdas that communicate via a database. One lambda will insert a new customer record into a Customer table. The other lambda will respond to that customer record creation by creating the information required for a welcome email into a PendingEmails table.

# Before you start
To avoid a lot of complex pre-requisites, this workshop uses a single AWS account (**TBA**). In order to avoid the different groups clashing with eachother, each group will be assigned an animal name that they will use as the prefix for all the different resources they create as part of this exercise (DynamoDB tables, lambdas, microservices, etc.)

The session leaders will provide you with a password for the AWS user you will use to create all your resources.

The supporting artefacts for the exercises can be found in the public repository https://github.com/andylongshaw/serverless

# Getting ready

1. Make sure you can log into the AWS console for the account using the AWS user for your group: \<MyAnimal\>Admin
1. Use the main console search bar to locate the individual consoles you will need during this exercise:
1.  lambda (Compute -> Lambda)
1.  DynamoDB (Database -> DynamoDB)
1.  API gateway (***TBA***)
1.  Cloud Formation (***TBA***)

# Create and test a simple microservice
In this part, you will create a simple microservice based on a lambda that is callable through the API gateway

1. Locate the cloudformation folder in the github repository. Make sure you have the two cloud formation template files on your local disk.

1. In the AWS console, navigate to the Cloud Formation console.

1. Create a new Cloud Formation Stack based on the instructions below

    > ***TBA***

    > Select the file spa2017-apigateway-lambda.template

1. In the AWS console, navigate to the Lambda console and locate the lambda you just created (\<MyAnimal\> ***TBA***)

1. Examine the different tabs on the lambda

    > ***TBA*** - code, configuration

1. ***TBA*** - test it with default contents

    > Load the test file from disk/github DynamoDB_microservice_message_insert.json

1. ***TBA***- test it from the API gateway?



# Make your simple microservice store data in DynamoDB

1. Create a second Cloud Formation Stack based on the instructions below

    > ***TBA***

    > Select the file spa2017-dynamodb-lambda.template

    > \<My Animal\>DynamodbStack

    > \<My Animal\>


1. Replace the code in it with the example code from the repository

    > Open the file solutions/python/aws_lambda_wrapper.py

    > Click on the Code tab in your ***TBA*** lambda function

    > Paste the code from the file into the code box, completely replacing what was there before

    > Click the Save button

    > Review the code to make sure you can roughly follow what it does

1. In the AWS console, navigate to the DynamoDB console and examine the \<My Animal\>CustomerTable ***CHECK_NAME***

    > Items

1. Go back to the ***TBA*** lambda function and change the 'table_name' variable to be ***TBA***

1. Run the test twice - once to insert a record and once to retrieve it

    > DynamoDB_microservice_message_insert.json

    > DynamoDB_microservice_message_retrieve.json

1. In the DynamoDB console, go see the data

**HERE**
use the pre-provided create customer and retrieve customer JSON files in your test, try adjusting the json files to add/retrieve different records


inserts a row in a DynamoDB database table (\<MyAnimal\>Customer) in response to a REST message.

# Create and test the Customer Email event handler
In this part you will create a lambda that will react to the writing of the Customer record by updating a second table (PendingEmails).

1. Create \<MyAnimal\>PendingEmails table in DynamoDB with a primary key (Partition Key) of 'emailId'
    > In the AWS Console, select Database -> DynamoDB -> Create Table
    > Enter the name of the table and the primary key - leave all other options as default
1. Alter the **\<MyAnimal\>Customer** table in DynamoDB so that it generates an event stream when records are inserted
    > Find the table in the AWS Console and click on it
    > Select Overview -> Stream Details -> Manage Stream -> old and new images

    Breadcrumbs from here...

    Dynamodb process stream python
    Table: Animal customer
    Starting pos: latest
    Function name: ZebraCustomerWelcomeEmail
    Role: ZebraRole

    Test event: DyanmoDb update
    IAM: add AmazonDynamoDBFullControl to Animal Role
**HERE**

# Call the Customer microservice from a command line client

Python 3 installed locally
sudo pip3 install boto3
sudo pip3 install requests


OR


1. Install the AWS CLI on your laptop following [these instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
1.  Take care to use the configuration file advice on the http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html page, not the regular CLI instructions

use the CLI API
