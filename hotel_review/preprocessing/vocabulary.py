import pandas as pd

hotel = pd.read_csv('./hotel_0.csv')

# 0번째 칼럼 제거
edithotel = hotel.drop(hotel.columns[[0]],axis = 'columns')

# 부정적인리뷰만 가지고 오기
neg = edithotel[['Negative_Review']] #(10311477,1)

# txt 파일로 변환 => 전처리 용이를 위함
negtxt = neg.to_csv('neg.txt', index = False, header = None, sep = "," )


#부정적인 리뷰 txt 데이터를 문장단위로 읽어온다.
n = open("../neg.txt")
lines =n.readlines()
neglines = str(lines).lower()

negative = neglines.replace(",", "").replace("\n", "").replace(".", "").replace("'","").replace("?","").replace("!","").replace("\\n","").replace("[","").replace("]","")
negative = negative.split(" ")
# print(len(negative)) 19634563

neg_voca = set(negative) #중복제거
# print(len(neg_voca)) # 69875

#긍정적인 리뷰
p = open("../pos.txt")
lines = p.readlines()
poslines = str(lines).lower()

positive = poslines.replace(",", "").replace("\n", "").replace(".", "").replace("'","").replace("?","").replace("!","").replace("\\n","").replace("[","").replace("]","")
positive = positive.split(" ")
pos_voca = set(positive) #중복제거
# print(len(pos_voca)) #64581

#공통된
common_vocab = pos_voca & neg_voca #23061
common_vocab = list(common_vocab)


pos_encoded = [common_vocab.index(x) if x in common_vocab else None for x in pos_voca]

# for x in zip(pos_encoded, pos_voca):
#     print(x)

neg_encoded = [common_vocab.index(x)if x in common_vocab else None for x in neg_voca]

# for y in zip(neg_encoded, neg_voca):
#     print(y)


#  방법 1 길이를 동일하게 맞춰주기
# pos_encoded = [x for x in pos_encoded if x !=None]
# neg_encoded = [y for y in neg_encoded if y !=None]

# print(len(pos_encoded)) #31646
# print(len(neg_encoded)) #31646


from sklearn.feature_extraction.text import TfidfVectorizer


token_dict = dict()

token_dict['pos'] = poslines
token_dict['neg'] = neglines

tfidf = TfidfVectorizer()
tfs = tfidf.fit_transform(token_dict.values())
print(token_dict.values())
print(tfidf.vocabulary_)

for x in tfidf.get_feature_names():
    print(x,":",tfidf.vocabulary_[x])


sentence = "good hotel"
resp = tfidf.transform([sentence])
print(resp)






