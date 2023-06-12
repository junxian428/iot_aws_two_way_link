import boto3
import urllib3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    #http = urllib3.PoolManager()
    #r = http.request('GET', 'https://junxian428.github.io/')
    #r.data
    # b'User-agent: *\nDisallow: /deny\n'
    #r.status
    # 200
    response = client.put_item(
        TableName = 'raspiData_v3',
        Item = {
            'timestamp': {'S': event['timestamp']},
            'distance': {'N': str(event['distance'])},
            'status': {'S': event['status']}
        }
    )

    # Initialize AWS IoT Data Plane client
    iot_data_client = boto3.client('iot-data')

    # Publish message to an AWS IoT topic
    #topic = 'your-iot-topic'
    message = 'Hello, IoT!'
    response = iot_data_client.publish(topic="Hello", qos=1, payload=message)

    # Print response
    print(response)

    # Return a response to the Lambda function
    return {
        'statusCode': 200,
        'body': 'Message published to AWS IoT topic'
    }
