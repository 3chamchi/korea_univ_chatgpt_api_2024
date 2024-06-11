# section23
# 네이버 기사 가져오기 함수
# 뉴스 기사 요약 및 키워드 추출 실습

# 1. ChatGPT API 패키지 불러오기
from bs4 import BeautifulSoup
import requests
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''
# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

# 4. 뉴스 기사 제목, 내용 입력
print('>>>> 뉴스 기사 요약, 키워드 추출기 <<<<')

news_url = input('기사 URL : ')
system_content = '뉴스 내용을 입력하여 내용 요약과 주요 키워드를 추출합니다.'

requests = requests.get(news_url)  # 입력 받은 URL 소스코드 가져오기
soup = BeautifulSoup(requests.content)  # HTML 코드 파싱을 위한 변수(객체) 생성
tag_article_contetns = soup.find(id="articleContetns")  # 특정 요소 검색
news_content = tag_article_contetns.text  # 불필요한 내용 제거, 텍스트 사용

# 5. ChatGPT API 요청, 응답 변수 생성
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': news_content},
    ]
)

# 6. 응답 메시지 출력
print(response.choices[0].message.content)
