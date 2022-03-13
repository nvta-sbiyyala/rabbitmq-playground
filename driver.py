import sys
import time


def main(argv):
    print("Hello World!")
    while True:
        print("Spinlock....")
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
