from dicts_and_indexes import *
from imports import *

N = 6348910  # num of documents in the curpus
to_return = 100


def inverted_cosine_similaruty_tfidf_title(query_tokens, index):
    similarity_dict = dict()  # doc_id : cosine similarity
    query_w = Counter(query_tokens)  # weights of words in the query
    query_norm = 1 / len(query_tokens)  # 1 / |q|
    docs_norm = dict()  # doc_id: 1 / |di|
    for term in set(query_tokens):
        if term in index.words:
            query_term_w = query_w[term]
            posting_list = read_posting(term, index)
            df = index.df[term]
            idf = np.log(N / df)
            for doc_id, freq in posting_list:
                if doc_id == 0:
                    continue
                docs_norm[doc_id] = 1 / DL_body[doc_id]
                tf = freq / DL_body[doc_id]
                w = tf * idf
                similarity_dict[doc_id] = similarity_dict.get(doc_id, 0) + w * query_term_w
    for doc_id in similarity_dict.keys():
        similarity_dict[doc_id] = similarity_dict[doc_id] * query_norm * docs_norm[doc_id]
    similarity_list = similarity_dict.items()  # [(doc_id, similarity_score)]
    sorted_similarity_list = sorted(similarity_list, key=lambda x: -x[1])[:to_return]
    sorted_similarity_list_with_title = [(doc[0], id_title_dict[doc[0]]) for doc in sorted_similarity_list]
    return sorted_similarity_list_with_title
