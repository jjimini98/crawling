import requests
import re
from bs4 import BeautifulSoup

url = "https://homepage.sch.ac.kr/sch/04/04061100.jsp"

req = requests.get(url)
html = req.text

li = []
intro = BeautifulSoup(html,'html.parser')

dele = str(intro.find_all('p'))
dele = re.sub('<.+?>','',dele,0).strip()

li.append(dele)

f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\leesoonsin.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()