import requests
import json

def lambda_handler(event, context):

# Parse the value into the API Gateway and validate the status code


# Body of the response
    apiResponse = {}
    apiResponse['days_until_expiration'] = '3'
    apiResponse['is_valid'] = 'True'
    apiResponse['domain_name'] = 'google.com'

# HTTP Response Object
    httpResponse = {}
    httpResponse['statusCode'] = request.status_code
    httpResponse['body'] = json.dumps(apiResponse)
    print(httpResponse)

# Return the response object
    
    return httpResponse



