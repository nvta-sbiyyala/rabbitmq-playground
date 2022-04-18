import pika

from config import get_logger

logger = get_logger(__name__)


def publish():
    # Create a connection, say CN
    # Create a channel in CN, say CH
    # Create an Exchange
    # Publish the message
    # Close the connection
    # Automatically closes the channel

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

    for i in range(400):
        message = bytes(f"Hello {str(i)}", encoding="utf8")
        channel.basic_publish(exchange='br_exchange', routing_key='', body=message)
        logger.info("[x] sent %r" % message)

    channel.exchange_delete(exchange='br_exchange', if_unused=False)

    connection.close()


if __name__ == "__main__":
    publish()
