import sys

import pika

from config import get_logger

logger = get_logger(__name__)


def main():
    # create a connection, CN
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # create a channel in CN, say CH
    channel = connection.channel()

    # If the queue does not exist, create it in the channel
    channel.queue_declare(queue="queue1")

    def callback(ch, method, properties, body):
        logger.info(f"received {body}")

    # Associate a callback with the message queue
    channel.basic_consume(queue="queue1", on_message_callback=callback, auto_ack=True)

    # Start consuming the message
    logger.info("[*] waiting for the messages. To exit press Ctrl+C")
    # Blocking call
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted")
        sys.exit(0)
