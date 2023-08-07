import json
import boto3
from botocore.config import Config
import logging
import boto3


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)







my_config = Config(
    region_name = 'us-west-2',
)

def receiver(event, context):
    

    
    sqs = boto3.client('sqs')
    queueUrl = 'https://sqs.ap-south-1.amazonaws.com/033509534972/test'
  
    data = sqs.receive_message(
        QueueUrl = queueUrl,
       MaxNumberOfMessages = 1,
    VisibilityTimeout = 10,
    WaitTimeSeconds = 0,
    )

    logger.info("Output",data["Messages"][0]['Body'])
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Producer",
                "data": data["Messages"][0]['Body']
            }
        ),
    }
