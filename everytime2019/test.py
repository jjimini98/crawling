from selenium import webdriver

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.everytime.kr/login")
driver.find_element_by_name('userid').send_keys('jjimini98')
driver.find_element_by_name('password').send_keys('dbwlals!!77')
driver.find_element_by_xpath("""//*[@id="container"]/form/p[1]/input""").click()