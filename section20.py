# section20
# 뉴스 기사 요약 및 키워드 추출 실습

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = 'sk-proj-g39lId2sEO2zqQln5DPJT3BlbkFJME8eLWpFpIAIHr3QmQyR'
# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

# 4. 뉴스 기사 제목, 내용 입력
print('''>>>> 뉴스 기사 요약, 키워드 추출기 <<<<
※ 뉴스, 기사 내용을 입력하시면 내용 요약과 주요 키워드를 추출해드립니다.\n''')
news_content = input('뉴스/기사 내용 : ')
system_content = '뉴스 내용을 입력하여 내용 요약과 주요 키워드를 추출합니다. 요약은 200자로 내외로 [요약], [주요 키워드] 항목을 답변하세요.'

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
