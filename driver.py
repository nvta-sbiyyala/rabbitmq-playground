import sys
import time

from config import get_logger

logger = get_logger(__name__)


def main(argv):
    logger.info("Hello World!")
    while True:
        logger.info("Spinlock....")
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
