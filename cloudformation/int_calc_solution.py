import datetime
import sys
def process_api_call(params):
   x = int(params['x'])
   y = int(params['y'])
   operator = params['operator']
   result = None
   if (operator == "add"):
       result = x + y
   elif (operator == "sub"):
       result = x - y
   return result

def lambda_handler(event, context):
    returnCode = 200
    result = process_api_call(event['queryStringParameters'])
    #result = 'lambda ' + context.function_name + ' was called at ' + datetime.datetime.now().strftime('%c')
    print(result)
    return {
      'statusCode': returnCode,
      'body': '{0}'.format(result)
    }

