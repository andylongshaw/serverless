# Objective
To create two AWS lambdas that communicate via a database. One lambda will insert a new customer record into a Customer table. The other lambda will respond to that customer record creation by creating the information required for a welcome email into a PendingEmails table.

# Before you start
To avoid a lot of complex pre-requisites, this workshop uses a single AWS account (**TBA**). In order to avoid the different groups clashing with eachother, each group will be assigned an animal name that they will use as the prefix for all the different resources they create as part of this exercise (DynamoDB tables, lambdas, microservices, etc.)

The session leaders will provide you with a password for the AWS user you will use to create all your resources.

The supporting artefacts for the exercises can be found in the public repository https://github.com/andylongshaw/serverless

# Getting ready

1. Make sure you can log into the AWS console for the account using the AWS user for your group: \<MyAnimal\>Admin

**TBA** Try the Hello world example first

# Create and test the Customer microservice
In this part, you will create a simple microservice that inserts a row in a DynamoDB database table (\<MyAnimal\>Customer) in response to a REST message.

1. Create \<MyAnimal\>Customer table in DynamoDB with a primary key (Partition Key) of 'customerId'
    
    > In the AWS Console, select Database -> DynamoDB -> Create Table
    
    > Enter the name of the table and the primary key - leave all other options as default
    
1. Create a API gateway-based microservice lambda
    
    > In the AWS Console, select Compute -> Lambda -> Create a Lmabda Function
    
    > Select a blueprint -> Select runtime Python 3.6 -> microservice-http-endpoint-python
    
    > Configure triggers -> set API Name to \<MyAnimal\>Microservice -> Next
    
    > Configure function -> set Name to \<MyAnimal\>Customer -> set Role Name to \<MyAnimal\>Role
    
    > Review and create lambda

1. Replace the code in it with the example code from the repository
    
    > Open the file solutions/python/aws_lambda_wrapper.py
    
    > Click on the Code tab in your lambda function
    
    > Paste the code from the file into the code box, replacing what was there before
    
    > Click the Save button
    
    > Review the code to make sure you understand what it does

1. 

**HERE**
use the pre-provided create customer and retrieve customer JSON files in your test, try adjusting the json files to add/retrieve different records

# Create and test the Customer Email event handler
In this part you will create a lambda that will react to the writing of the Customer record by updating a second table (PendingEmails).

1. Create \<MyAnimal\>PendingEmails table in DynamoDB with a primary key (Partition Key) of 'emailId'
    > In the AWS Console, select Database -> DynamoDB -> Create Table
    > Enter the name of the table and the primary key - leave all other options as default
1. Alter the **\<MyAnimal\>Customer** table in DynamoDB so that it generates an event stream when records are inserted
    > Find the table in the AWS Console and click on it
    > Select Overview -> Stream Details -> Manage Stream
**HERE**

# Call the Customer microservice from a command line client

Python 3 installed locally
sudo pip3 install boto3
sudo pip3 install requests


OR


1. Install the AWS CLI on your laptop following [these instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
1.  Take care to use the configuration file advice on the http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html page, not the regular CLI instructions

use the CLI API
