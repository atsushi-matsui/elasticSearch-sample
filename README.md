# What
Sample elastic search.

### Required
- python3
- pipenv
- homebrew

### Scripts
- init
```
bash ./script/init.bash 
```
- stop
```
bash ./script/stop.bash
```

### Login
- elastic search start test.
```
curl localhost:9200
```
- login to kibana.
```
http://localhost:5601/
```


### Tips
|  ES  |  RDBMS  |
| ---- | ---- |
|  index  |  database  |
|  type  |  table  |
|  document  |  row  |
|  field  |  column  |
|  mapping  |  schema  |


### Refs
[elasticsearch-py](https://github.com/elastic/elasticsearch-py)

[python sample](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html#ex-search)
