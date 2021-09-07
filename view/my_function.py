import time

from utils import decorator


@decorator
def wait_one():
    time.sleep(1)
