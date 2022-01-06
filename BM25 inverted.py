from imports import *

# TODO: get title by id
# TODO: DL

# abgdl calc:
num_docs = len(DL)
sum_lengths = sum(DL.values())
avgdl = int(sum_lengths / num_docs)

def inverted_BM25_similaruty(query_tokens,body_index,words, pls, k1, b):
  N = 6348910 # num of documents in the curpus
  similarity_dict = dict() # doc_id : cosine similarity

  for term in query_tokens:
    index_in_pls = words.index(term)
    posting_list = pls[index_in_pls]

    df = body_index.df[term]
    q_i_IDF = np.log((N - df + 0.5) / (df + 0.5) + 1)

    for doc_id, freq in posting_list:
      f_ti_D = freq
      len_of_D = DL[doc_id]
      w = q_i_IDF * ((f_ti_D * (k1 + 1)) / (f_ti_D + k1 * (1 - b + b * (len_of_D / avgdl))))
      similarity_dict[doc_id] = similarity_dict.get(doc_id, 0) + w

  similarity_list = similarity_dict.items() # [(doc_id, similarity_score)]
  sorted_similarity_list = sorted(similarity_list, key = lambda x: -x[1])[:100]
  sorted_similarity_list_with_title = [(doc[0], get_title_by_id(doc[0])) for doc in sorted_similarity_list]
  return sorted_similarity_list_with_title