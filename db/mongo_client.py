import yaml
from pymongo import MongoClient

with open("db_config.yaml", "r") as f:
    config = yaml.safe_load(f)


client = MongoClient(host=config['host'], port=config['port'])


__all__ = (
    "client"
)
