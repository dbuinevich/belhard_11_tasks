import inspect
import time

from db import mongo


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполнено {func.__name__}")
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
        taburetka = {
            'module': inspect.getmodule(func).__name__,
            'function': func.__name__,
            'args': str(args),
            'kwargs': str(kwargs),
            'start_time': str(start_time),
            'end_time': str(end_time),
            'duration': str(end_time - start_time)
        }
        daba = mongo.benchmarks
        collection = daba.functions_benchmark
        collection.insert_one(taburetka)
        return result
    return wrapper
