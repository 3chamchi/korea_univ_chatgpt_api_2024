# section19
# 인터뷰 질문지 작성

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI
# 2. API 키 변수 생성
api_key = ''

# 데이터 수집을 위한 API 연동
seed_data = {
    '세종시': '맑음',
    '대전시': '비 조금',
}
# 전처리

# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)
# 4. 인터뷰 질문지를 위한 조건 입력
user_text1 = input('목적 : ')
user_text2 = input('주제 : ')
user_text3 = input('청중 : ')

system_text = '날씨 데이터 : ' + seed_data + '다음 날씨를 고려하여 입력받는 지역의 여행지를 제시해줘'

system_text = '''
당신은 기자입니다. 
다음 내용을 기반으로 인터뷰 질문지를 작성합니다.
질문지의 항목은 최소 10개이고 두 가지 버전으로 답변합니다.'''

# 5. ChatGPT API 요청, 응답 변수 생성
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': system_text},
        {'role': 'user', 'content': f'''
        목적 : {user_text1},
        주제 : {user_text2},
        청중 : {user_text3}'''},
    ]
)
# 6. 응답 메시지 출력
print(response.choices[0].message.content)
