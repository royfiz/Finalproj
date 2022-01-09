from dicts_and_indexes import *
from get_page_rank_backend import *
from get_pageviews_backend import *

to_return = 100

def search_backend(query_tokens):
    title_scores = inverted_BM25_similaruty_title(query_tokens, index_title)
    body_scores = inverted_BM25_similaruty_body(query_tokens, index_body)
    anchor_scored = search_anchor_for_opt(query_tokens, index_anchor)

    scores_dict = {"title": title_scores, "body": body_scores,
                   "anchor": anchor_scored, "pageview": norm_pageviews_dict, "pagerank": norm_pagerank_dict}
    res = merge_results(scores_dict, weights_dict)  # 100 united scores
    res = [(x[0], id_title_dict[x[0]]) for x in res]  # give titles
    return res


#  calculating avgdl for BM25:
num_docs = len(DL_title)
sum_lengths = 0
for val in DL_title.keys(): sum_lengths += DL_title[val]
avgdl_title = sum_lengths / num_docs
num_docs = len(DL_body)
sum_lengths = 0
for val in DL_body.keys(): sum_lengths += DL_body[val]
avgdl_body = sum_lengths / num_docs


# title:
def inverted_BM25_similaruty_title(query_tokens, index, k1=2, b=1):
    N = 6348910  # num of documents in the curpus
    similarity_dict = dict()  # doc_id : cosine similarity
    for term in query_tokens:
        if term in index.words:
            posting_list = read_posting(term, index)
            df = index.df[term]
            q_i_IDF = np.log((N - df + 0.5) / (df + 0.5) + 1)
            for doc_id, freq in posting_list:
                if doc_id == 0:
                    continue
                f_ti_D = freq
                len_of_D = DL_title[doc_id]
                w = q_i_IDF * ((f_ti_D * (k1 + 1)) / (f_ti_D + k1 * (1 - b + b * (len_of_D / avgdl_title))))
                similarity_dict[doc_id] = similarity_dict.get(doc_id, 0) + w
    return similarity_dict


# body:
def inverted_BM25_similaruty_body(query_tokens, index, k1=1, b=0.22222):
    N = 6348910  # num of documents in the curpus
    similarity_dict = dict()  # doc_id : cosine similarity
    for term in query_tokens:
        if term in index.words:
            posting_list = read_posting(term, index)
            df = index.df[term]
            q_i_IDF = np.log((N - df + 0.5) / (df + 0.5) + 1)
            for doc_id, freq in posting_list:
                if doc_id == 0:
                    continue
                f_ti_D = freq
                len_of_D = DL_body[doc_id]
                w = q_i_IDF * ((f_ti_D * (k1 + 1)) / (f_ti_D + k1 * (1 - b + b * (len_of_D / avgdl_body))))
                similarity_dict[doc_id] = similarity_dict.get(doc_id, 0) + w
    return similarity_dict


# anchor:
def search_anchor_for_opt(query_tokens, index):
    relavent_docs = {}
    for term in np.unique(query_tokens):
        if term in index.words:
            list_of_docs = read_posting(term, index)
            for dest_id, flag in list_of_docs:
                if dest_id == 0:
                    continue
                relavent_docs[dest_id] = relavent_docs.get(dest_id, 0) + 10
    return relavent_docs


# page views:
norm_pageviews_dict = dict()
for page in pageviews_dict:
    norm_pageviews_dict[page] = pageviews_dict[page] ** (0.25) / 3

# page rank:
norm_pagerank_dict = dict()
for page in pagerank_dict:
    norm_pagerank_dict[page] = np.sqrt(pagerank_dict[page]) / 3

# weights_dict:
weights_dict = {"title": 1, "body": 1,
                "anchor": 1, "pageview": 1, "pagerank": 0}


# merge:
def merge_results(scores_dict, weights_dict):
    # united for query: [(doc_id, united_score)]
    united_list = []
    score_types = list(scores_dict.keys())
    # all relevant docs for query:
    doc_ids = set()
    for score_type in score_types:
        if score_type in ["pageview", "pagerank"]:
            continue
        else:
            doc_ids = doc_ids.union(set(scores_dict[score_type].keys()))
    # calc united score
    for doc_id in doc_ids:
        doc_united_score = 0
        for score_type in score_types:
            w = weights_dict[score_type]
            if doc_id in scores_dict[score_type]:
                doc_united_score += scores_dict[score_type][doc_id] * w
        united_list.append((doc_id, doc_united_score))
    # sort:
    united_list_sorted = sorted(united_list, key=lambda x: -x[1])[:to_return]
    return united_list_sorted
