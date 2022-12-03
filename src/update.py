from datetime import datetime
from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX


client = Elasticsearch(CONNECT)

doc = {
    'author': 'author_name',
    'text': 'Interensting modified content...',
    'timestamp': datetime.now(),
}
resp = client.update(index=SAMPLE_INDEX, id=1, document=doc)
print(resp['result'])
