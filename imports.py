import sys
from collections import Counter, OrderedDict
import itertools
from itertools import islice, count, groupby
import pandas as pd
import numpy as np
import os
import math
import re
from operator import itemgetter
import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
from time import time
from timeit import timeit
from pathlib import Path
import pickle


#nltk.download('stopwords')


import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.ml.feature import Tokenizer, RegexTokenizer

from nltk.corpus import stopwords
xxx = 3
# import csv
# mydict = dict()
# with open('pagerank.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     for rows in reader:
#         mydict[int(rows[0])] = float(rows[1])
#
# output = open('pagerank_dict.pkl', 'wb')
# pickle.dump(mydict, output)
# output.close()


with open( f'{"pagerank_dict"}.pkl', 'rb') as f:
  pagerank_dict  = pickle.load(f)

pagerank_dict[3434750]
