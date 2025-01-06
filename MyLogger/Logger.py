from pika import BlockingConnection, ConnectionParameters
import json

log = []

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f'Message Recieved: {json.loads(body)}')
    log.append(message)

def Logger():
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='events')
    channel.basic_consume(queue='events', on_message_callback=callback, auto_ack=True)
    print('Waiting Messages...')
    channel.start_consuming()
