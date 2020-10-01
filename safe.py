from bs4 import BeautifulSoup
import requests
import re

url = "https://homepage.sch.ac.kr/sch/04/04060200.jsp"

req = requests.get(url)
html = req.text


li = []
soup = BeautifulSoup(html,'html.parser')
dele = str(soup.find_all('p'))
dele = re.sub('<.+?>','',dele,0).strip()
#name = soup.select("#jwxe_main_content > div.jwxe_root > div:nth-child(2) > h3 > img")
#introduction = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div > div:nth-child(3) > p")
#contents =  soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div > div.jwxe_div > div")

#name = str(name)
#introduction = str(introduction)
#contents = str(contents)
li.append(dele) # 하는일 부분이 삭제됨;;
#li.append(introduction)
#li.append(contents)

f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\safe.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

