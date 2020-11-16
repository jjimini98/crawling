# 깃허브에있는 긍정 부정 단어를 들고온다.
# https://github.com/shekhargulati/sentiment-analysis-python/blob/master/opinion-lexicon-English/positive-words.txt
# http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

import numpy as np
import pandas as pd

dic = pd.read_csv("./positive-words_dictionary.txt")

