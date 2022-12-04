# What
Sample elastic search.

## Required
- python3
- pipenv
- homebrew

## Scripts
### init

1. start elasticSearch and kibana.
```
source ./script/init.bash 
```
2. create venv.
```
pipenv shell
```
3. install modules.
```
pipenv install
```

### stop
1. exit from venv.
```
exit
```
2. stop elasticSearch and kibana.
```
bash ./script/stop.bash
```

## Commands
- elastic search health check.
```
cd ./src
python3 sample.py
```
- login to kibana.
```
http://localhost:5601/
```


## Tips
|  ES  |  RDBMS  |
| ---- | ---- |
|  index  |  database  |
|  type  |  table  |
|  document  |  row  |
|  field  |  column  |
|  mapping  |  schema  |


## Refs
[elasticsearch-py](https://github.com/elastic/elasticsearch-py)

[python sample](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html#ex-search)
