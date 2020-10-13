import pandas as pd
import matplotlib.pyplot as plt

# 데이터 가져오기  데이터가 커서 그런지 개느리다

origin_hotel = pd.read_csv('hotels_reviews.csv') #<class 'pandas.core.frame.DataFrame'>
hotel= origin_hotel.copy()

# hotel 데이터의 전체적인 정보 출력
#print(hotel.info())

# 데이터의 결측치 확인

#print(hotel.isna().sum()) # lat/lng에서 각각 3268개의 NA값이 확인됨


# 데이터의 결측치 처리 결측치는 각 열의 평균으로 하려고 했지만, 결과가 오지게 안나와서 그냥 0 으로 처리 아무래도 5000개의 데이터의 평균을 구하기 쉽지 않았을거다.
hotel_fillna = hotel.fillna(0)
#print(hotel_fillna.isna().sum()) #결측치를 -으로 처리 !

# 결측치를 없앤 값을 다시 hotel dataframe에 대입
hotel = hotel_fillna

# 리뷰어가 어디가 제일 많은지 봐보자
reviewer = hotel['Reviewer_Nationality'].value_counts().sort_values(ascending=False).head(20)
#print(reviewer)


# 평이 좋은 호텔 시각화
worst_hotels =hotel.groupby('Hotel_Name')['Reviewer_Score'].mean().sort_values(ascending=True).head(5)
worst_hotels.plot(kind="bar",color="Red")
_=plt.xlabel('Worst Hotels according to Reviews')
_=plt.ylabel('Average Review Score')
plt.show()

# 평이 안좋은 호텔 시각화
good_hotels =hotel.groupby('Hotel_Name')['Reviewer_Score'].mean().sort_values(ascending=False).head(5)
good_hotels.plot(kind="bar",color="blue")
_=plt.xlabel('good Hotels according to Reviews')
_=plt.ylabel('Average Review Score')
plt.show()
