from elasticsearch import Elasticsearch
from setting import CONNECT, SAMPLE_INDEX

es = Elasticsearch(CONNECT)

resp = es.search(index=SAMPLE_INDEX, query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    #print(hit["_source"])
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
