
from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt
import pandas as pd


es_ip = "http://127.0.0.1:9200"
es = Elasticsearch(es_ip)

query_str = {"size": 0,"aggregations": {"result": { "terms": {"field": "host.name.keyword","order": [{"_count": "desc"}]}}}}
res = es.search(index="winlogbeat", body=query_str)
result = res["aggregations"]["result"]["buckets"]

event_pd = pd.DataFrame(result, columns=["key", "doc_count"], index = ["DESKTOP-T3V8EOP","LAPTOP-O5NUGDHI","DESKTOP-QLB0CEN"])
ax = event_pd.plot(x="key", y="doc_count", kind="bar",figsize=(8,4))

plt.xlabel("host_name")
plt.ylabel("counts")
plt.xticks(rotation=0)
plt.show()