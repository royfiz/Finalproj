from imports import *
import csv

pagerank_dict = dict()
with open('pagerank.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        pagerank_dict[int(rows[0])] = float(rows[1])


def get_page_rank_by_id(id):
    return pagerank_dict[id]

vec_get_page_rank_by_id = np.vectorize(get_page_rank_by_id)


def get_page_rank_backend(articles_ids):
    articles_ids = np.array(articles_ids)
    ans = vec_get_page_rank_by_id(articles_ids)
    return list(ans)


