#긍정부정 두 열을 합치는 코드
import pandas as pd

from afinn import Afinn

data = pd.read_csv("./hotel_edit.csv")

#긍정과 부정 리뷰를 띄어쓰기로 합친 새로운 열 total_review 생성
data['total_review'] = data['Negative_Review']+" "+data['Positive_Review']

#필요없는 열 모두 제거
del data['Unnamed: 0']
del data['Negative_Review']
del data['Positive_Review']
del data['Reviewer_Score']

# No negative, No positive, Nothing 은 빈칸으로 replace
for x in data['total_review']:
    if 'No Negative' in x:
       data['total_review']= data['total_review'].str.replace("No Negative","-")
    if 'No Positive' in x:
        data['total_review']= data['total_review'].str.replace("No Positive","-")
    if 'Nothing' in x:
        data['total_review'] = data['total_review'].str.replace('Nothing',"-")

afinn = Afinn()

# 새로운 파일 edit_hotel_afinn.csv 생성 후 한 문장씩 읽어들임.
# 맨 처음 실행해서 파일을 만들고 그다음부터는 그냥 주석처리해서 쓰심 됩니다
re_data= open("./edit_hotel_afinn.csv", "w")
for x in data['total_review']:
    re_data.writelines(x)
    re_data.write("\n")
    re_data.write(str(afinn.score(x)))
    re_data.write(" ")
re_data.close()

# 긍정부정 합친 문장에 대한 점수를 태깅하려고 함
# scoredata = pd.read_csv("./hotel_afinn.csv")


# 근데 결과가 이상함 다 -4.0 이 나온다.?? 한 번 파일을 확인해봐야한다.
# file = open("hotel_afinn.csv","r")
#
# lines = file.readlines()
# score = []
# for y in lines:
#     score = afinn.score(y)
# print(score)

