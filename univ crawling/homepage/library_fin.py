from bs4 import BeautifulSoup
import requests
import re

def change(name):
    name = name[0].text
    name = name.replace("/", "")
    name = str(name)

    return name

url = "https://homepage.sch.ac.kr/sch/04/04060100.jsp"


req = requests.get(url)
html = req.text

soup = BeautifulSoup(html,'html.parser')

li = []


intro = soup.select("#jwxe_main_content > div.jwxe_root")

one = soup.select("[class=jwxe_html]")

two = soup.select("[class=jwxe_text]")

for a,b in zip(one,two):
    dele = str(intro.find_all('div'))
    dele = re.sub('<.+?>', '', dele, 0).strip()
    li.append(dele)



f = open('/univ crawling/homepage/library_fin.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()
