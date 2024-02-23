"""
- 네이버 뉴스 데이터 크롤링 하기
    - 언론사별 랭킹뉴스 3곳 일일랭킹 제목 3개 뽑기 (리스트로 만들어서 넣기)
    - 일주일치 분량 뽑기
    - 데이터프레임으로 만들어서 csv 저장하기
"""

import pprint
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

URL = "https://news.naver.com/main/ranking/popularDay.naver"

# browser = webdriver.Chrome()
# browser.get(URL)

# soup = BeautifulSoup(browser.page_source, "lxml")

res = requests.get(URL, timeout=30)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

news = soup.find("div", attrs={"class": "_officeCard _officeCard0"})
news_dict = {}
news = news.find_all("div", attrs={"class": "rankingnews_box"})

for elem in news:
    company_name = elem.find("strong", attrs={"class": "rankingnews_name"}).get_text()
    titles = elem.find_all("a", attrs={"class": "list_title nclicks('RBP.rnknws')"})
    title = [t.get_text() for t in titles]
    news_dict[company_name] = title

# df = pd.DataFrame.from_dict(data=news_dict, orient='columns')

pprint.pprint(news_dict)

df = pd.DataFrame.from_dict(data=news_dict, orient='columns')

df.to_csv('data.csv', encoding='utf=-8')

# input("종료하려면 Enter를 입력하세요")
