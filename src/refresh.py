from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX

es = Elasticsearch(CONNECT)
es.indices.refresh(index=SAMPLE_INDEX)
