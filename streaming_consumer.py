import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='streaming_notifications')

    def callback(ch, method, properties, body):
        print(f" [x] Received notification: {body.decode()}")

    channel.basic_consume(queue='streaming_notifications', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for notifications. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()