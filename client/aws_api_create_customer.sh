#!/bin/bash

REST_API_ID=opf5rml8y5
RESOURCE_ID=m6e1nu
CUSTOMER_ID=A3456
CUSTOMER_NAME="Fred Lloyd"

aws apigateway test-invoke-method --rest-api-id $REST_API_ID --resource-id $RESOURCE_ID --http-method POST --path-with-query-string "" --body "{ \"customerId\":\"$CUSTOMER_ID\",\"name\":\"$CUSTOMER_NAME\"}"
