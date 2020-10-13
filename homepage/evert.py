from bs4 import BeautifulSoup
import requests


#크롤링 된 텍스트를 string 으로 변환하고 슬래시 제거
def change(name):
    name = name[0].text
    #name = name.replace("/", "")
    name = str(name)

    return name

#한국문화콘텐츠학과

url = "https://everytime.kr/389132"

req = requests.get(url)
html= req.text

li = []
soup = BeautifulSoup(html,'html.parser')
junsungwoon = soup.select(" #container > div.wrap.articles > article:nth-child(2) ")

print(junsungwoon)