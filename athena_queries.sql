create database iot_db;

create external table iot_data (
    device_id string,
    temperature double,
    humidity double,
    timestamp string
)

row format serde 'org.openx.data.jsonserde.JsonSerDe'
Location 's3://iot-stream-storage-12345/iot-data/';


select * from iot_data limit 10;