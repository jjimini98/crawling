from nltk import PorterStemmer, LancasterStemmer, word_tokenize
import pandas as pd
# import nltk
# nltk.download('stopwords')

hotel = pd.read_csv('./hotel_0.csv')

# 0번째 칼럼 제거
edithotel = hotel.drop(hotel.columns[[0]],axis = 'columns')
edithotel = hotel.iloc[[0,1,2,3,4,5,6,7,8,9],:]

# 부정적인리뷰만 가지고 오기
neg = edithotel[['Negative_Review']] #(10311477,1)
# txt 파일로 변환 => 전처리 용이를 위함
negtxt = neg.to_csv('neg.txt', index = False, header = None, sep = "," )

#부정적인 리뷰 txt 데이터를 문장단위로 읽어온다.
f = open("./neg.txt")
lines = f.readlines()
lines = str(lines)


from nltk import PorterStemmer, LancasterStemmer , word_tokenize
lines = str(lines)

# tokenization
tokens = word_tokenize(lines)
print(len(tokens))

#porter stemmer
porter = PorterStemmer()
porter_stems = [porter.stem(t) for t in tokens]
print(porter_stems)

#lancaster stemmer
lancaster = LancasterStemmer()
lancaster_stems = [lancaster.stem(t) for t in tokens ]
print(lancaster_stems)


#stopword
import nltk

#단어길이가 3 이하 생략
word_filter = [e for e in tokens if len(e)>=3]
print(len(word_filter))
print(word_filter[:20])

#생략된 단어들 출력
word_skipped = [e for e in tokens if len(e)<3]
print(word_skipped[:20])

#nltk 에서 제공하는 stopword 목록
stopwords = nltk.corpus.stopwords.words('english')
print(len(stopwords))
print(stopwords[:20])

words = [w for w in word_filter if w.lower() not in stopwords]
print(len(words))
print(words[:20])



# 긍정적인 리뷰만 가지고 오기
pos = edithotel[['Positive_Review']]
postxt = pos.to_csv('pos.txt',index=False,header=None, sep = ",")

#부정적인 리뷰 txt 데이터를 문장단위로 읽어온다.
f = open("./pos.txt")
lines = f.readlines()
lines = str(lines)

from nltk import PorterStemmer, LancasterStemmer , word_tokenize
lines = str(lines)

# tokenization
tokens = word_tokenize(lines)
print(len(tokens))

#porter stemmer
porter = PorterStemmer()
porter_stems = [porter.stem(t) for t in tokens]
print(porter_stems)

#lancaster stemmer
lancaster = LancasterStemmer()
lancaster_stems = [lancaster.stem(t) for t in tokens ]
print(lancaster_stems)


#stopword
import nltk

#단어길이가 3 이하 생략
word_filter = [e for e in tokens if len(e)>=3]
print(len(word_filter))
print(word_filter[:20])

#생략된 단어들 출력
word_skipped = [e for e in tokens if len(e)<3]
print(word_skipped[:20])

#nltk 에서 제공하는 stopword 목록
stopwords = nltk.corpus.stopwords.words('english')
print(len(stopwords))
print(stopwords[:20])

words = [w for w in word_filter if w.lower() not in stopwords]
print(len(words))
print(words[:20])