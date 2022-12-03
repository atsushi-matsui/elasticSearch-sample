from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX

client = Elasticsearch(CONNECT)

client.delete(index=SAMPLE_INDEX, id=1)
