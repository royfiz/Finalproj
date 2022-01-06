from imports import *


# Load the page views file
PAGE_VIEW_FILE_NAME = "pageviews-202108-user.pkl"
with open(PAGE_VIEW_FILE_NAME, 'rb') as f:
  wid2pv = pickle.loads(f.read())


def get_page_view_by_id(id):
    return wid2pv[id]

vec_get_page_rank_by_id = np.vectorize(get_page_view_by_id)

# Function def
def get_pageview_beckend(articles_ids):
  num_articles = len(articles_ids)
  ans = [0 for i in range(num_articles)]
  for i in range(num_articles):
    article_id = articles_ids[i]
    ans[i] = wid2pv[article_id]
  return ans

def get_page_view(articles_ids):
    articles_ids = np.array(articles_ids)
    ans = vec_get_page_rank_by_id(articles_ids)
    return list(ans)

test_articles = [5878274, 7712754, 3632887, 600744, 59804426, 63743203, 34443176, 4838455, 11011780, 4822278]
print(get_page_view(test_articles))