# !pip install selenium
# !pip install bs4

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 스타벅스 홈페이지의 매장 검색 사이트에 접속

browser = webdriver.Chrome('chromedriver.exe')
url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'

browser.get(url)

# 지역에서 "서울"을 찾아서 클릭 : xpath를 이용하는 경우

xpath = '''//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a'''
browser.find_element_by_xpath(xpath).click()


# 지역에서 "서울"을 찾아서 클릭 : css를 이용하는 경우

# seoul_btn = '''#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'''
# browser.find_element_by_css_selector(seoul_btn).click()

# HTML 분석

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
# soup

# 첫 번째 매장 정보 출력
starbucks_soup_list = soup.select('li.quickResultLstCon')
# starbucks_soup_list




starbucks_store = starbucks_soup_list[0]

name = starbucks_store.select('strong')[0].text.strip()
lat = starbucks_store['data-lat'].strip()
lng = starbucks_store['data-long'].strip()
store_type = starbucks_store.select('i')[0]['class'][0][4:]
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]

print("매장이름 : ", name)
print("매장위도 : ", lat)
print("매장경도 : ", lng)
print("매장타입 : ", store_type)
print("매장주소 : ", address)
print("매장번호 : ", tel)




# 전체 매장 정보를 출력

# starbucks_list = []

# for i in starbucks_soup_list :
#     name = i.select('strong')[0].text.strip()
#     lat = i['data-lat'].strip()
#     lng = i['data-long'].strip()
#     store_type = i.select('i')[0]['class'][0][4:]
#     address = str(i.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
#     tel = str(i.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
#     
#     starbucks_list.append([name,lat,lng,store_type,address,tel])
# starbucks_list[3]



# 엑셀 파일로 저장

columns = ['매장명','위도','경도','매장타입','매장주소','매장전화']

seoul_starbucks_df = pd.DataFrame(starbucks_list, columns = columns)
seoul_starbucks_df