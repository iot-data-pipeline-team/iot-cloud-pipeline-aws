# Real-Time IoT Streaming Analytics Pipeline on AWS

## Project Overview

This project demonstrates a cloud-native real-time IoT analytics pipeline built on AWS.

Simulated IoT sensor data is continuously generated and streamed through AWS services, stored in a data lake, queried using SQL, and visualized using Tableau.

The project was built as part of Data Engineering and Business Intelligence learning and preparation for ITI Data Management.

---

## Architecture

IoT Sensor Simulator (Python)

↓

Amazon Kinesis Data Streams

↓

AWS Lambda

↓

Amazon S3 Data Lake

↓

Amazon Athena

↓

Tableau Dashboard

---

## Technologies Used

### AWS Services

* Amazon Kinesis Data Streams
* AWS Lambda
* Amazon S3
* Amazon Athena

### Visualization

* Tableau Desktop

### Programming

* Python
* SQL

---

## Project Components

### Producer
![alt text](<Screenshot (1856).png>)
The producer simulates IoT sensor telemetry data.

Generated attributes:

* device_id
* temperature
* humidity
* timestamp

Data is pushed to Amazon Kinesis every 2 seconds.

---

### Streaming Layer
![alt text](<Screenshot (1859).png>)
Amazon Kinesis Data Streams receives incoming sensor events and acts as the real-time ingestion layer.

Stream Name:

iot-stream

---

### Processing Layer
![alt text](<Screenshot (1857).png>)
AWS Lambda consumes records from Kinesis.

Processing steps:

1. Decode Kinesis payload
2. Parse JSON data
3. Store records in Amazon S3

Function Name:

iot-consumer

---

### Data Lake
![alt text](<Screenshot (1858).png>)
Amazon S3 stores incoming telemetry as JSON files.

Folder Structure:

iot-data/

---

### Analytics Layer
![alt text](<Screenshot (1854).png>)
Amazon Athena is used to query sensor data directly from S3.

Database:

iot_db

Table:

iot_data

Example Query:

SELECT *
FROM iot_data
LIMIT 10;

---

### Visualization Layer
![alt text](<Screenshot (1853).png>)
Tableau connects to Athena using the Amazon Athena ODBC Driver.

Dashboard visualizations include:

* Temperature trends
* Humidity trends
* Sensor activity monitoring

---

## Sample Data

{
"device_id": "sensor_3",
"temperature": 29.92,
"humidity": 42.71,
"timestamp": "2026-05-31T12:51:26.321549"
}

---

## Future Improvements

* Real-time dashboards using OpenSearch Dashboards
* Data aggregation using AWS Glue
* Historical analytics with Redshift
* Infrastructure as Code using Terraform
* Multi-cloud implementation using GCP Pub/Sub and BigQuery

---

## Author

Abdelrahman Malek

Data Engineering / Business Intelligence Learning Project

