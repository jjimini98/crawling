from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

# 에브리타임 로그인 정보
driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.everytime.kr/login")
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
jebal = soup.select('large')

driver.find_element_by_name('userid').send_keys('jjimini98')
driver.find_element_by_name('password').send_keys('dbwlals!!77')
driver.find_element_by_xpath("""//*[@id="container"]/form/p[1]/input""").click()
