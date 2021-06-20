import pika

# credentials = pika.PlainCredentials('user', 'yqN8jqo9x8')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.cuiqingcai.com', port=5672, credentials=credentials))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
