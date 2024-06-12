# section24
# ChatGPT API 언어 번역기 ver3
# 번역할 내용을 입력받아 2개 이상의 번역 제공

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

# 4. 번역할 내용 입력
user_content = input('번역할 내용 : ')

# 5. ChatGPT API 요청, 응답 변수 생성
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': '''당신은 전문 번역가입니다. 
        다음 입력한 내용을 영어, 중국어, 힌디어, 스페인어, 프랑스어, 아랍어로 번역하십시오. 
        응답은 번역한 언어별로 구분하여 표현합니다.'''},
        {'role': 'user', 'content': user_content},
    ]
)

# 6. 응답 메시지 출력
print(response.choices[0].message.content)
