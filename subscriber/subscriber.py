import traceback

import boto3
import paho.mqtt.subscribe as subscribe

firehose = boto3.client('firehose', region_name='us-east-1')


def on_message_post_to_kinesis(client, userdata, message):
    try:
        response = firehose.put_record(DeliveryStreamName='home',
                                     Record={'Data': message.payload + b"\n"})
        print(response)
    except:
        traceback.print_exc()
        quit(0)


if __name__ == "__main__":
    subscribe.callback(on_message_post_to_kinesis, "garden/sensors")
