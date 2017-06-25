# Extension 1 - Access customer records from the API gateway console

1. Retrieve a customer record via the API Gateway

    > Navigate to the API Gateway console
    
    > Locate the *GET* method for your service

1. Run the *GET* method but this time provide a *customerId* parameter in the *Query Strings* box, e.g. "customerId=?????" where "?????" is the id of any customer you have created in your *CustomerTable*

# Extension 2 - Access the customer service from a client

1. You can use either curl or write a small client

1. Invoke the API through its URL

    > Navigate to the API Gateway and click Stages -> LATEST

    > You can find the base URL at the top of this tab

    > Create the invocation URL by adding "/customer?customerId=?????" to the base URL where "?????" is the id of any customer you have created in your *CustomerTable*

    > For example: *curl https://mr2u24f25a.execute-api.eu-west-1.amazonaws.com/LATEST/customer?customerId=A1234*

# Extension 3 - Create customer records from the API gateway console

1. Add a POST method in the API Gateway

    > Actions -> Create Method -> POST
    
    > Click the checkbox for "Use lambda proxy integration"
    
    > Set Lambda region "eu-west-1"
    
    > Set Lambda function to *\<MyAnimal\>-ApiHandlerLambda*
    
    > Click "Save"
    
    > Click "OK" to add permission

    > In the Method Execution diagram, click "Integration Request"
    
    > In "Body Mapping Templates" click the "+" to "Add mapping template"
    
    > Paste the following as the template body:
    
    <pre>
    {
        "httpMethod": "$context.httpMethod",
        "body" : $input.json('$')
    }
    </pre>
        
    > Run the *POST* method "Test" with a message body something like this:
    
    <pre>
    {
        "customerId": "A1299",
        "name": "Freddo Bloggszzy"
    }
    </pre>
    
    > Examine your response
    
    > Check the CustomerTable and the PendingEmailTable for the new records
    
That's it!
