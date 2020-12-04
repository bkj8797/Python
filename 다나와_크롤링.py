from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from tqdm.notebook import tqdm
import warnings

# 경고메시지 숨기기
# warnings.filterwarnings(action='ignore')를 action='default'로 변경하면 경고메시지가 나타난다.
warnings.filterwarnings(action='ignore')



def get_search_page_url(keyword, page):
    return 'http://search.danawa.com/dsearch.php?query={}&volumeType=allvs&page={}&limit=30&sort=saveDESC&list=list&boost=true&addDelivery=N&tab=goods&tab=goods'.format(keyword, page)

keyword = input("검색어를 입력해주세요 : ")
pages = int(input("검색할 페이지숫자를 입력해주세요 : "))

page = 1
url = get_search_page_url(keyword, page)
print(url)



def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try: 
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try: 
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list = ''
        try: 
            price = int(prod_item.select('p.price_sect > a > strong')[0].text.strip().replace(",",""))
        except:
            price = 0
        prod_data.append([title, spec_list, price])
    return prod_data



# 윈도우에서는 .exe 추가해주세요
driver = webdriver.Chrome('chromedriver') 
driver.implicitly_wait(3)

total_page = pages
prod_data_total = []



print("처리중")
for page in tqdm(range(1,total_page+1)):
    driver.get(url)
    url = get_search_page_url(keyword, page)
    time.sleep(2)
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
    prod_item_list = get_prod_items(prod_items)
    
    prod_data_total = prod_data_total + prod_item_list


data = pd.DataFrame(prod_data_total)
data.columns = ['상품명', '스펙 목록', '가격']
data = data.sort_values(['가격'], ascending=[True])
data.to_excel('danawa_{}_crawling_result.xlsx'.format(keyword), index=False)
driver.close()
print('완료')

ㅇ