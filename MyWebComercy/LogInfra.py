from pika import BlockingConnection, ConnectionParameters
import json

def sendToLog(message):
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='events')
    channel.basic_publish(exchange='', routing_key='events', body=json.dumps(message))
    connection.close()
