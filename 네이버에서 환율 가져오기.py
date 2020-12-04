from bs4 import BeautifulSoup
import urllib.request as req

#HTML 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

#HTML 분석하기
soup = BeautifulSoup(res, "html.parser")

#원하는 데이터 추출하기 ---
results = soup.select("span.value")
print("달러 =", results[0].string+"원")
print("엔화 =", results[1].string+"원")
print("유로 =", results[2].string+"원")