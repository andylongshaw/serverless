# Objective
To create two AWS lambdas that communicate via a database. One lambda will insert a new customer record into a Customer table. The other lambda will respond to that customer record creation by inserting the information required for a welcome email into a PendingEmail table.

# Before you start
To cut out a lot of complex pre-requisites, this workshop uses a single AWS account. In order to avoid the different groups clashing with eachother, each group will be assigned an animal name that they will use as the prefix for all the different resources they create as part of this exercise (DynamoDB tables, lambdas, microservices, etc.)

The session leaders will provide you with a password for the AWS user you will use to create all your resources.

The supporting artefacts for the exercises can be found in the public repository https://github.com/andylongshaw/serverless

# Getting ready

1. Make sure you can log into the AWS console for the account using the AWS user for your group: *\<MyAnimal\>Admin*

    > Navigate to https://612280087062.signin.aws.amazon.com/console
    
    > Enter the username and password provided to log in

1. Use the main console search bar to locate the individual consoles you will need during this exercise:

    > lambda (Compute -> Lambda)

    > DynamoDB (Database -> DynamoDB)

    > API gateway (Application Services -> API Gateway)

    > CloudFormation (Management Tools -> CloudFormation)

# Create and test a simple microservice
In this part, you will create a simple microservice based on a lambda that is callable through the API gateway

1. Locate the *cloudformation* folder in the github repository. Make sure you have the two CloudFormation *.template* files on your local disk.

1. Create a new CloudFormation Stack based on the instructions below

    > In the AWS Console, navigate to the CloudFormation console

    > Click "Create Stack"

    > Select Template -> Choose a template -> Upload a template to Amazon S3 -> Choose File

    > Select the file *spa2017-apigateway-lambda.template*

    > Specify details -> Stack name - set this to *\<MyAnimal\>APIGatewayStack*

    > Parameters -> namePrefixParameter - change this from *spa2017* to *\<MyAnimal\>*

    > Options -> just click "Next"

    > Review -> click the "I acknowledge that..." checkbox -> Create

    > Wait until the *Status* of this new stack in the list of Stacks is *CREATE_COMPLETE*

1. In the AWS console, navigate to the Lambda console and locate the lambda you just created (*\<MyAnimal\>-ApiHandlerLambda*)

1. Examine the different tabs on the lambda

    > Code, configuration, monitoring

1. Test invoking your lambda in the lambda console

    > Click the "Test" button
    
    > Check that the selected test message is the one listed as "Hello World" in the dropdown list
    
    > Click "Save and test"
    
    > Review the execution results at the bottom of the page

1. Test it from the API gateway

    > Navigate to the API Gateway console
    
    > Select the *\<MyAnimal\>-LambdaApi*
    
    > Under */customer* click "GET"
    
    > Click the "Test" link near the lightning flash
    
    > Click the "Test" button
    
    > Examine the response/logs


# Make your simple microservice store data in DynamoDB
In this part you will update your lambda function to write a record to the *CustomerTable*.

1. Create a second Cloud Formation Stack based on the instructions below

    > In the AWS Console, navigate to the CloudFormation console

    > Select "Create Stack"

    > Select Template -> Choose a template -> Upload a template to Amazon S3 -> Choose File

    > Select the file *spa2017-dynamodb-lambda.template*

    > Specify details -> Stack name - set this to *\<MyAnimal\>DynamoDBStack*

    > Parameters -> namePrefixParameter - change this from *spa2017* to *\<MyAnimal\>*

    > Options -> just click "Next"

    > Review -> click the "I acknowledge that..." checkbox -> Create

    > Wait until the *Status* of the stack in the list of Stacks is *CREATE_COMPLETE*

1. In the AWS console, navigate to the DynamoDB console and examine the *\<MyAnimal\>-CustomerTable*

    > Click "Tables" in the left-hand navigation bar

    > Click on the table name

    > Examine the information in the *Overview* tab

    > Look at the *Items* tab - this is where you can see your records appear

1. In the AWS console, navigate to the Lambda console and replace the code in your API gateway lambda with the example code from the repository

    > Open the file *solutions/python/aws_lambda_customer_rest.py*

    > Click on the *Code* tab in your *\<MyAnimal\>-ApiHandlerLambda* lambda function

    > Paste the code from the file into the code box, completely replacing what was there before

    > Click the "Save" button

    > Review the code to make sure you can roughly follow what it does

1. Change the *table_name* variable to be *\<MyAnimal\>-CustomerTable* and click "Save"

1. Run the test to insert a record

    > Click the "Actions" button and select "Configure test event"

    > Locate the *messages* folder in the github repository and paste the contents of the *customer_rest_message_insert.json* file into the input test event box, completely replacing what was there before

    > Click "Save and Test"

    > Examine the execution result and the log output

1. Navigate to the DynamoDB console and check that it contains a Customer matching the data in the message file above

1. Run the test to retrieve the record

    > Navigate to the *\<MyAnimal\>-ApiHandlerLambda* lambda

    > Click the "Actions" button and select "Configure test event"

    > Locate the *messages* folder in the github repository and paste  the contents of the *customer_rest_message_retrieve.json* file into the input test event box, completely replacing what was there before

    > Click "Save and Test"

    > Examine the execution result and the log output

1. Try adjusting the json files to add/retrieve different records


# Create and test the Customer Email trigger
In this part you will create a lambda that will react to the writing of the *CustomerTable* record by updating a second table (*PendingEmailTable*).

1. In the DynamoDB console, navigate to the *\<MyAnimal\>-PendingEmailTable*

    > Click "Tables" in the left-hand navigation bar

    > Click on the table name

    > Examine the information in the *Overview* tab

    > Look at the *Items* tab - this is where you can see your records appear

1. Now navigate to the *\<MyAnimal\>-CustomerTable* and look at the *Triggers* tab

    > You should see an entry for a lambda called *\<MyAnimal\>-DynamoChangeHandlerLambda*

1. Click through the lambda link in the *Trigger* and populate the trigger lambda with the example code from the repository

    > Open the file *solutions/python/aws_lambda_email_trigger.py*

    > Click on the *Code* tab in your *\<MyAnimal\>-DynamoChangeHandlerLambda* lambda function

    > Paste the code from the file into the code box, completely replacing what was there before

    > Click the "Save" button

    > Review the code to make sure you can roughly follow what it does

1. Change the *table_name* variable to be *\<MyAnimal\>-PendingEmailTable* and click "Save"

1. Run the test to insert a record

    > Click the "Actions" button and select "Configure test event"

    > Locate the *messages* folder in the github repository and paste  the contents of the *new_customer_trigger_message.json* file into the input test event box, completely replacing what was there before

    > Click "Save and Test"

    > Examine the execution result and the log output

1. Navigate to the DynamoDB console and check that the *\<MyAnimal\>-PendingEmailTable* contains a pending email matching the data in the message file above

# Run the lambda combination end-to-end

1. In the AWS console, navigate back to the *\<MyAnimal\>-ApiHandlerLambda* lambda

1. Edit the test to change it to the POST/create version of the message and change the *customerId* and name to something distinctive

1. Run the test

1. Check you get the right customer record in *\<MyAnimal\>-CustomerTable*

1. Check you get an appropriate email record in *\<MyAnimal\>-PendingEmailTable*

# What now?

Well, you could either try the [extension exercises](extensions.md) or you could go and get a well-earned coffee.


