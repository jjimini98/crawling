from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("../chromedriver.exe")
# 에브리타임 자유게시판
driver.get('https://everytime.kr/389132/v/60370414')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
arti = soup.select('#container > div.wrap.articles > article > a > h2')

for a in arti:
    print(a.text.strip())