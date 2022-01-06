from imports import *

# TODO: get title by id
# TODO: DL

def get_title_by_id(id):
  dic = {1:"11", 2:"22",3:"33"}
  return dic[id]

def inverted_cosine_similaruty_tfidf(query_tokens,body_index,words, pls):
  N = 6348910 # num of documents in the curpus
  similarity_dict = dict() # doc_id : cosine similarity
  query_w = Counter(query_tokens) # weights of words in the query
  query_norm = 1 / len(query_tokens) # 1 / |q|
  docs_norm = dict() # doc_id: 1 / |di|
  for term in query_tokens:
    query_term_w = query_w[term]
    index_in_pls = words.index(term)
    posting_list = pls[index_in_pls]
    df = body_index.df[term]
    idf = np.log(N / df)
    for doc_id, freq in posting_list:
      docs_norm[doc_id] = 1 / DL[doc_id]
      tf = freq / df
      w = tf * idf
      similarity_dict[doc_id] = similarity_dict.get(doc_id, 0) + w * query_term_w
  for doc_id in similarity_dict.keys():
    similarity_dict[doc_id] = similarity_dict[doc_id] * query_norm * docs_norm[doc_id]
  similarity_list = similarity_dict.items() # [(doc_id, similarity_score)]
  sorted_similarity_list = sorted(similarity_list, key = lambda x: -x[1])[:100]
  sorted_similarity_list_with_title = [(doc[0], get_title_by_id(doc[0])) for doc in sorted_similarity_list]
  return sorted_similarity_list_with_title