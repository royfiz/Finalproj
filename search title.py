from imports import *

# TODO: get title by id

def search_title(query_tokens, words, pls):
  '''This function is for wraper to implement search_title and search_anchor'''
  relavent_docs = {}
  for term in np.unique(query_tokens):
    if term in words:
      list_of_doc = pls[words.index(term)]
      for doc_id, freq in list_of_doc:
        relavent_docs[doc_id] = relavent_docs.get(doc_id,0) + 1
  relavent_docs_list_sorted = sorted(relavent_docs.keys(), key = lambda doc_id: - relavent_docs[doc_id])
  relavent_docs_list_sorted_with_title = [(i, get_title_by_id(i)) for i in relavent_docs_list_sorted]
  return relavent_docs_list_sorted_with_title










