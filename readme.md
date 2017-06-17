# Objective
To create two AWS lambdas that communicate via a database. One lambda will insert a new customer record into a Customer table. The other lambda will respond to that customer record creation by creating the information required for a welcome email into a PendingEmails table.

# Before you start
To avoid a lot of complex pre-requisites, this workshop uses a single AWS account (**TBA**). In order to avoid the different groups clashing with eachother, each group will be assigned an animal name that they will use as the prefix for all the different resources they create as part of this exercise (DynamoDB tables, lambdas, microservices, etc.)

The session leaders will provide you with a password for the AWS user you will use to create all your resources.

**TBC** - will we pre-provide their admin user rather than give them root creds and have them provision it?
   Create IAM user(s) in account http://docs.aws.amazon.com/lambda/latest/dg/setting-up.html#setting-up-iam

# Getting ready

1. Make sure you can log into the AWS console for the account using the AWS user for your group: \<MyAnimal\>Admin
1. Install the AWS CLI on your laptop following [these instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
1.  Take care to use the configuration file advice on the http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html page, not the regular CLI instructions

# Create the Customer microservice
will be part of a simple microservice that inserts a row in a database table (Customers) in response to a REST message. T

Create \<MyAnimal\>Customer table

# Create the Customer Email event handler

he second will react to the writing of the record by updating a second table (PendingEmails)

