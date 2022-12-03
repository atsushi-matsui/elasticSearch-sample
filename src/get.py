from datetime import datetime
from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX

# Connect to 'http://localhost:9200'
es = Elasticsearch(CONNECT)

resp = es.get(index=SAMPLE_INDEX, id=1)
print(resp['_source'])
