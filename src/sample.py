from datetime import datetime
from elasticsearch import Elasticsearch
from setting import CONNECT


# Connect to 'http://localhost:9200'
es = Elasticsearch(CONNECT)


# Call an API, in this example `info()`
resp = es.info()
print(resp)
