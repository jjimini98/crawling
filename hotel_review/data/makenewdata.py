import pandas as pd

#데이터를 다시 다운받으니까 되네;;
hotel = pd.read_csv("./Hotel_Reviews.csv")

print(hotel.shape)
print(hotel.info())

print(hotel.isnull().sum())

#칼럼이름제거
hotel_0 = hotel.drop(['Hotel_Address','Additional_Number_of_Scoring','Review_Date','Average_Score','Hotel_Name','Reviewer_Nationality',
                      'Total_Number_of_Reviews','Total_Number_of_Reviews_Reviewer_Has_Given','Tags','days_since_review',
                      'lat','lng','Review_Total_Negative_Word_Counts','Review_Total_Positive_Word_Counts'], axis='columns')

hotel_0 = hotel_0.dropna()

hotel_0.to_csv('hotel.csv',mode= 'a')
