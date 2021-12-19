import csv

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import os

es = Elasticsearch('localhost:9200',http_auth=('elastic','changeme'))
for path,dirs,files in os.walk(('.\\error_test')):
    for file in files:
        with open(path+'\\'+file, encoding='UTF-8') as f:
            reader =csv.DictReader(f)
            helpers.bulk(es, reader, index='ai_2021')


