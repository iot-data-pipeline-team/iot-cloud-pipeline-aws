import json
import time
import random
from datetime import datetime

import boto3

kinesis = boto3.client("kinesis", region_name = "us-east-1")

while True:
        data = {
                "device_id": f"sensor_{random.randint(1,5)}",
                "temperature": round(random.uniform(20, 40), 2),
                "humidity": round(random.uniform(30, 90), 2),
                "timestamp": datetime.utcnow().isoformat()
        }

        print(data)

        kinesis.put_record(
                StreamName = "iot-stream",
                Data = json.dumps(data),
                PartitionKey = "sensor"
        )

        time.sleep(2)
