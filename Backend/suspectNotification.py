
import logging
import boto3
import json

logger= logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session(region_name="us-east-1")
sns_client = session.client('sns')


def lambda_handler(event, context):
    body = json.loads(event["body"])
    
    suspect_name = body['suspect']
    response = sns_client.publish(
        
        PhoneNumber= body['phone_number'],
        Message = "Suspect: %s has been seen"%suspect_name,
        MessageAttributes = {
            'AWS.SNS.SMS.SenderID':{
                'DataType': 'String',
                'StringValue':'SENDERID'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType':'String',
                'StringValue': 'Promotional'
            }
        }
    )
    
    logger.info(response)
    return {
        'statusCode':200,
        'body': json.dumps({'msg':"Messages has been sent"})
    }
