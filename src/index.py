from datetime import datetime
from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX

es = Elasticsearch(CONNECT)

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index=SAMPLE_INDEX, id=1, document=doc)
print(resp['result'])
