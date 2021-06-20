import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello2',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ),
                      body=message)
print(" [x] Sent %r" % message)
