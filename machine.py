from bs4 import BeautifulSoup
import requests
import re

url = "https://homepage.sch.ac.kr/sch/04/04060300.jsp"

req = requests.get(url)
html = req.text

li = []
intro = BeautifulSoup(html,'html.parser')
print(intro.text)
dele = str(intro.find_all('p'))
dele = re.sub('<.+?>','',dele,0).strip()

li.append(dele)

f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\machine.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()