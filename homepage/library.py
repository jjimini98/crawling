from bs4 import BeautifulSoup
import requests
import re

url = "https://homepage.sch.ac.kr/sch/04/04060100.jsp"

req = requests.get(url)
html= req.text

li = []
soup = BeautifulSoup(html,'html.parser')
name = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_html > h3 > img')
introduction = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(1) > div > p')
contents = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2)')

name=str(name)
introduction = str(introduction)
contents = str (contents)


li.append(name)
li.append(introduction)
li.append(contents)


f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\library.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()
