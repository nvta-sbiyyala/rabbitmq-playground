import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO)


def get_logger(name):
    return logging.getLogger(name)
