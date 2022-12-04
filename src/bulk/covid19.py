import csv
from os.path import abspath, join, dirname, exists
from tqdm import tqdm
import urllib3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

CONNECT = "http://localhost:9200"
COVID19 = (
    "https://data.cityofnewyork.us/resource/rc75-m7u3.csv"
)
DATASET_PATH = join(dirname(abspath(__file__)), "covid19.csv")
CHUNK_SIZE = 16384
INDEX = "covid19"

def _download_dataset():
    if not exists(DATASET_PATH):
        http = urllib3.PoolManager()
        resp = http.request("GET", COVID19, preload_content=False)
    else:
        with open(DATASET_PATH) as f:
            count = 0
            for _ in f:
                count += 1
            return count -1
        
    if resp.status != 200:
        raise RuntimeError("Could not download dataset")
        
    with open(DATASET_PATH, mode="wb") as f:
        chunk = resp.read(CHUNK_SIZE)
        while chunk:
            f.write(chunk)
            chunk = resp.read(CHUNK_SIZE)
                
    with open(DATASET_PATH) as f:
        return sum([1 for _ in f]) - 1

def _create_index(client):
    client.indices.create(
        index=INDEX,
        body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "date_of_interest": {"type": "date_nanos"},
                    "case_count": {"type": "integer"},
                    "probable_case_count": {"type": "integer"},
                    "hospitalized_count": {"type": "integer"},
                    "death_count": {"type": "integer"},
                }
            },
        },
        ignore=400,
    )

def _generate_actions():
    with open(DATASET_PATH, mode="r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            doc = {
                "date_of_interest": row["date_of_interest"],
                "case_count": int(row["case_count"]),
                "probable_case_count": int(row["probable_case_count"]),
                "hospitalized_count": int(row["hospitalized_count"]),
                "death_count": int(row["death_count"]),
            }

            yield doc
    

def main():
    number_of_docs = _download_dataset()
    es = Elasticsearch(
        CONNECT
    )
    print("Creating an index...")
    _create_index(es)
    
    print("Indexing documents...")
    progress = tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=es, index=INDEX, actions=_generate_actions(),
    ):
        progress.update(1)
        successes += ok
    
    print("Indexed %d/%d documents" % (successes, number_of_docs))

if __name__ == '__main__':
    main()
