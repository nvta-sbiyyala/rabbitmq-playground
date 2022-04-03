import sys
import time

import pika


def produce(argv):
    # create a connection, CN
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # create a channel in CN, say CH
    channel = connection.channel()

    # [Optional] Create an Exchange and Specify the bindings
    # This step is not required in this example, uses default Exchange

    # If the queue does not exist, create it in the channel
    channel.queue_declare(queue="queue1")

    # Publish
    channel.basic_publish(exchange="", routing_key="queue1", body=b"Hello world!")
    print("Published message")

    # Close the connection, and that auto closes the channel
    connection.close()


if __name__ == "__main__":
    while True:
        produce(sys.argv)
        time.sleep(5)
