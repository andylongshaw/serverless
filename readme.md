# Objective
To create two AWS lambdas that communicate via a database. One lambda will insert a new customer record into a Customer table. The other lambda will respond to that customer record creation by creating the information required for a welcome email into a PendingEmails table.

# Before you start
To avoid a lot of complex pre-requisites, this workshop uses a single AWS account (**TBA**). In order to avoid the different groups clashing with eachother, each group will be assigned an animal name that they will use as the prefix for all the different resources they create as part of this exercise (DynamoDB tables, lambdas, microservices, etc.)

The session leaders will provide you with a password for the AWS user you will use to create all your resources.

# Getting ready

1. Make sure you can log into the AWS console for the account using the AWS user for your group: \<MyAnimal\>Admin

**TBA** Try the Hello world example first

# Create and test the Customer microservice
In this part, you will create a simple microservice that inserts a row in a DynamoDB database table (\<MyAnimal\>Customer) in response to a REST message.

1. Create \<MyAnimal\>Customer table in DynamoDB with a primary key (Partition Key) of 'customerId'
    > In the AWS Console, select Database -> DynamoDB -> Create Table
    > Enter the name of the table and the primary key - leave all other options as default
1. 

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
