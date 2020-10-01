from bs4 import BeautifulSoup
import requests
import re

url = "https://homepage.sch.ac.kr/sch/04/04060100.jsp"

req = requests.get(url)
html = req.text

soup = BeautifulSoup(html,'html.parser')

intro = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div")
intro = (intro[0].text)

content = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2)")
contents = content[0].text
contents = contents.replace("\n","")
contents = contents.replace("        	","")

#분명 selector 를 복사해올 땐 향설 고시원도 포함이었는데 여기로 옮기면 안보인다;

li = []

li.append(intro)
li.append(contents)


f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\library_prac.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#결과가 왜 이모양인지 모르겠다...........

