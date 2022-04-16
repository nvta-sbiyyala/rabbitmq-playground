import time

import pika

from config import get_logger

logger = get_logger(__name__)


def produce(ctr):
    # create a connection, CN
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # create a channel in CN, say CH
    channel = connection.channel()

    # [Optional] Create an Exchange and Specify the bindings
    # This step is not required in this example, uses default Exchange

    # If the queue does not exist, create it in the channel
    channel.queue_declare(queue="queue1")

    # Publish
    channel.basic_publish(exchange="", routing_key="queue1", body=bytes(f"Hello world #{ctr}", encoding="utf8"))
    logger.info("Published message")

    # Close the connection, and that auto closes the channel
    connection.close()


if __name__ == "__main__":
    counter = 1
    while True:
        produce(counter)
        time.sleep(5)
        counter += 1
