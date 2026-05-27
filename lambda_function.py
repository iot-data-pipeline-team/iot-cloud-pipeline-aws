import json 
import base64
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'iot-stream-storage-12345'

def lambda_handler(event, context):

    for record in event['Records']:
        payload = base64.b64decode(
            record['kinesis']['data']
        ).decode('utf-8')

        data = json.loads(payload)

        print("Received:", data)

        file_name = (
            f"iot-data/{datetime.utcnow().isoformat()}.json"
        )

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )

    return {'statusCode': 200}