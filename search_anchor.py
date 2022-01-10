from imports import *
from dicts_and_indexes import *


def search_anchor_backend(query_tokens, index):
    relavent_docs = {}
    for term in np.unique(query_tokens):
        if term in index.words:
            list_of_docs = read_posting(term, index)
            for dest_id, flag in list_of_docs:
                if dest_id == 0:
                    continue
                relavent_docs[dest_id] = relavent_docs.get(dest_id, 0) + 1
    relavent_docs_list_sorted = sorted(relavent_docs.keys(), key=lambda doc_id: - relavent_docs[doc_id])
    relavent_docs_list_sorted_with_title = [(i, id_title_dict[i]) for i in relavent_docs_list_sorted]
    return relavent_docs_list_sorted_with_title
