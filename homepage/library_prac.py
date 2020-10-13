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
#info = soup.find_all('div',attrs={'class':'jwxe_html'})
#tags = soup.find_all('div',attrs={'class' : 'jwxe_text'})


intro = soup.select("#jwxe_main_content > div.jwxe_root")

one = soup.select("[class=jwxe_html]")
two = soup.select("[class=jwxe_text]")

for a,b in zip(one,two): #class 속성값이 ~ 면
    print(a.text)
    print(b.text)

munhun = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(3) > p")
munhun_location = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > div:nth-child(1) > p")
munhun_site = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > div:nth-child(2) > p")
munhun_contents = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > div:nth-child(4) > p > span")
munhun_1 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(1) > div")
munhun_2 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(2) > div")
munhun_3 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(3) > div")
munhun_4 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(4) > div")
munhun_5 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(5) > div")
munhun_6 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(6) > div")
munhun_7 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(7) > div")
munhun_8 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(8) > div")
munhun_9 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(9) > div")
munhun_10 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(4) > div > ul > li:nth-child(10) > div")


#multi,multi_1 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(4) > div > p > span","#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(4) > ul > li:nth-child(1) > div")
multi_2 = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(4) > ul > li:nth-child(2) > div")




bookcafe = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(5) > ul > li:nth-child(1) > div")
theater = soup.select("#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(9)")

li = []

#li.append(change(intro))
#li.append(change(munhun))
#li.append(change(munhun_context))
#li.append(change(multi))
#li.append(change(bookcafe))
#li.append(change(theater))


#f = open('C:\\Users\\jimin\\PycharmProjects\\crawling\\library_prac.txt','w',encoding='utf-8')
#for c in li:
#    f.write(c)
#    f.write('\n')

#f.close()

#결과가 왜 이모양인지 모르겠다...........

