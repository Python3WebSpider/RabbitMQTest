import pika
import pickle
import requests

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape3'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


session = requests.Session()


def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {response.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')


while True:
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True)
    if body:
        print(f'Get {body}')
        request = pickle.loads(body)
        print(request)
        scrape(request)
