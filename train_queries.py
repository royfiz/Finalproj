import json
from sklearn.model_selection import train_test_split

print("fds")

f = open('queries_train.json')
''' 
    queries_to_relavent_docs is a dictionary of length 30 with -
          key: query (str)
          value: list of relavent documents id's (list)
'''
queries_to_relavent_docs = json.load(f)
f.close()


'''10 test queries and 20 train queries'''
train_queries, test_queries = train_test_split(list(queries_to_relavent_docs.keys()), test_size=10, shuffle=True)

for quer in test_queries:
    print(quer)