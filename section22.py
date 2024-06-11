# section21
# 네이버 기사 가져오기 함수
from bs4 import BeautifulSoup
import requests

# URL 페이지 소스코드 가져오기
url = "https://sports.news.nate.com/view/20240608n06169"
requests = requests.get(url)

# 페이지 요소 찾기
# id articleContetns
soup = BeautifulSoup(requests.content)
# print(soup.prettify())
# print(soup.find(id="articleContetns"))
tag_article_contetns = soup.find(id="articleContetns")
# print(tag_article_contetns)
print(tag_article_contetns.text)
