import pika
# from pika.spec
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.cuiqingcai.com', port=5672, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2', durable=True)

import time


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    print(type(ch), type(method), type(properties), type(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello2',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
