from db import mongo
from utils.func_bench import decorator


def class_decorator(cls):
    functions = {key: value for key, value in cls.__dict__.items() if callable(value)}
    for key, value in functions.items():
        with_decorator = decorator(value)
        stul = {'class_name': cls.__name__}
        daba = mongo.benchmarks
        collection = daba.class_functions_benchmark
        collection.insert_one(stul)
        setattr(cls, key, with_decorator)
    return cls
