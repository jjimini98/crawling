from bs4 import BeautifulSoup
import requests

url = "https://homepage.sch.ac.kr/sch/04/04060100.jsp"

req = requests.get(url)
html= req.text
#print(req)  #단순한 응답코드만 제공
#print(html)
li = []
soup = BeautifulSoup(html,'html.parser')
name = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_html > h3 > img')
introduction = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(1) > div > p')
contents = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2)')
#print(name)
#print(introduction[0].text)
#print(contents[0].text)
name=str(name)
introduction = str(introduction)
contents = str (contents)


li.append(name)
li.append(introduction)
li.append(contents)
print(type(contents))
#print(li)
f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\library.txt','w',encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()
#.text라고 치니까 이상한 코드가 같이 안뜬다!