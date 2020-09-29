from bs4 import BeautifulSoup
import requests

url = "https://homepage.sch.ac.kr/sch/04/04060100.jsp"

req = requests.get(url)
html= req.text
#print(req)  #단순한 응답코드만 제공
#print(html)

soup = BeautifulSoup(html,'html.parser')
name = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_html > h3 > img')
introduction = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(1) > div > p')
contents = soup.select('#jwxe_main_content > div.jwxe_root > div.jwxe_div > div:nth-child(2)')
print(name)
print(introduction[0].text)
print(contents[0].text)

#.text라고 치니까 이상한 코드가 같이 안뜬다!