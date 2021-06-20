import pika
import requests
import pickle

MAX_PRIORITY = 100
TOTAL = 100
QUEUE_NAME = 'scrape3'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)

for i in range(1, TOTAL + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    print('re', request)
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ),
                          body=pickle.dumps(request))
    print(f'Put request of {url}')
