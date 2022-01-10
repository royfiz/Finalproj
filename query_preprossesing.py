from nltk.corpus import stopwords
import nltk
import re

nltk.download('stopwords')

english_stopwords = frozenset(stopwords.words('english'))
corpus_stopwords = ["category", "references", "also", "external", "links",
                    "may", "first", "see", "history", "people", "one", "two",
                    "part", "thumb", "including", "second", "following",
                    "many", "however", "would", "became"]
corpus_stopwords = set(corpus_stopwords)
all_stopwords = english_stopwords.union(corpus_stopwords)
RE_WORD = re.compile(r"""[\#\@\w](['\-]?\w){2,24}""", re.UNICODE)


def query_preprosess(text):
    tokens = [token.group() for token in RE_WORD.finditer(text.lower())]
    ans = [word for word in tokens if word not in all_stopwords]
    return ans
