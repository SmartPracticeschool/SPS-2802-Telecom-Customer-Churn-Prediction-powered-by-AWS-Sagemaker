
import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')



def lambda_handler(event, context):
    print("Received event: " , json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    print("Data:",data)
     
    
    
    payload = data['data']
    
    print("Payload:",payload)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                        ContentType='text/csv',Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)

    if result>0.4:
        return 1
    else:
        return 0
    