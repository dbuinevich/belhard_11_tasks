import time

from utils import class_decorator


@class_decorator
class Waiting:
    def wait_two(self):
        time.sleep(2)

    def wait_three(self):
        time.sleep(3)
