import json
from ssl_checker import SSLChecker

SSLChecker = SSLChecker()


def lambda_handler(event, context):
    hostname = json.loads(event['body'])    
    args = {
    'hosts': [hostname["hostname"]]
        }
        
    res=SSLChecker.show_result(SSLChecker.get_args(json_args=args))
        
    half_data = json.loads(res)
    
    finaloutput = {} 
    try:
        hostName = half_data[hostname["hostname"]]["host"] 
        validDaysToExpire = half_data[hostname["hostname"]]["valid_days_to_expire"] 
        certValid = half_data[hostname["hostname"]]["cert_valid"] 
        
        finaloutput['domain_name'] = hostName
        finaloutput['days_until_expiration'] = validDaysToExpire
        finaloutput['is_valid'] = certValid
        return finaloutput
        
    except Exception as e:
        print(e)        
        return {"message":"your host name is incorrect or Something is wrong..."}