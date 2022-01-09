import pickle
from inverted_index_colab import *


# indexes read:
with open(f'{"index_text"}.pkl', 'rb') as f:
    index_body = pickle.load(f)
with open(f'{"title_index"}.pkl', 'rb') as f:
    index_title = pickle.load(f)
with open(f'{"indexses_index_anc"}.pkl', 'rb') as f:
    index_anchor = pickle.load(f)

# indexes attributes:
index_title.path = "postings_gcp_title"
index_anchor.path = "postings_gcp_anc"
index_body.path = "postings_gcp_text"

index_title.words = set(index_title.df.keys())
index_anchor.words = set(index_anchor.df.keys())
index_body.words = set(index_body.df.keys())

# read posting list:
TUPLE_SIZE = 6
BLOCK_SIZE = 1999998


def read_posting(word, index):
    b = []
    posting_list = []
    df = index.df[word]
    path = index.path
    locs = index.posting_locs[word]
    n_bytes = index.df[word] * TUPLE_SIZE
    for f_name, offset in locs:
        post_before = ""
        f = open(f"{path}/{f_name}", 'rb')
        f.seek(offset)
        lst = [n_bytes, BLOCK_SIZE - offset]
        if lst[0] <= (BLOCK_SIZE - offset):
            n_read = n_bytes
        else:
            n_read = BLOCK_SIZE - offset
        b.append(f.read(n_read))
        n_bytes -= n_read
        post_before = b''.join(b)
        for i in range(df):
            doc_id = int.from_bytes(post_before[i * TUPLE_SIZE:i * TUPLE_SIZE + 4], 'big')
            tf = int.from_bytes(post_before[i * TUPLE_SIZE + 4:(i + 1) * TUPLE_SIZE], 'big')
            posting_list.append((doc_id, tf))
        return posting_list


with open(f'{"Dl_body"}.pkl', 'rb') as f:
    DL_body = pickle.load(f)
with open(f'{"dl_title"}.pkl', 'rb') as f:
    DL_title = pickle.load(f)
with open(f'{"id_title_dict"}.pkl', 'rb') as f:
    id_title_dict = pickle.load(f)
