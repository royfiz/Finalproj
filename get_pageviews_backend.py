from imports import *

# Load the page views file
PAGE_VIEW_FILE_NAME = "pageviews-202108-user.pkl"
with open(PAGE_VIEW_FILE_NAME, 'rb') as f:
  pageviews_dict = pickle.loads(f.read())


def get_page_view_by_id(id):
    return pageviews_dict[id]

vec_get_page_rank_by_id = np.vectorize(get_page_view_by_id)

def get_page_view_backend(articles_ids):
    articles_ids = np.array(articles_ids)
    ans = vec_get_page_rank_by_id(articles_ids)
    return list(ans)


