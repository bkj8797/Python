from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

url = 'http://search.danawa.com/dsearch.php?k1=usb&module=goods&act=dispMain'

driver.get(url)

# 웹페이지의 HTML 정보 가져오기

from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

soup