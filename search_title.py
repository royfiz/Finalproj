from imports import *
from dicts_and_indexes import *

to_return = 100
def search_title_binary(query_tokens, index):
  relavent_docs = {}
  for term in np.unique(query_tokens):
    if term in index.words:
      list_of_docs = read_posting(term, index)
      for doc_id, freq in list_of_docs:
        if doc_id == 0:
          continue
        relavent_docs[doc_id] = relavent_docs.get(doc_id,0) + 1
  relavent_docs_list_sorted = sorted(relavent_docs.keys(), key = lambda doc_id: - relavent_docs[doc_id])[:to_return]
  relavent_docs_list_sorted_with_title = [(i, id_title_dict[i]) for i in relavent_docs_list_sorted]
  return relavent_docs_list_sorted_with_title










