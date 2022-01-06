from imports import *

# TODO: pagerank dict
page_rank_dict = {1: 11, 2:22, 3:33}

def get_page_rank_by_id(id):
    return page_rank_dict[id]

vec_get_page_rank_by_id = np.vectorize(get_page_rank_by_id)


def get_pagerank(articles_ids):
    articles_ids = np.array(articles_ids)
    ans = vec_get_page_rank_by_id(articles_ids)
    return list(ans)


