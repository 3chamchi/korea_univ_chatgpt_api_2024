# section21
# 영화 후기 감정 분석기

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI
# 2. API 키 변수 생성
api_key = 'sk-proj-g39lId2sEO2zqQln5DPJT3BlbkFJME8eLWpFpIAIHr3QmQyR'
# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

while True:
    # 4. 영화 후기 내용 입력
    user_content = input('후기 : ')

    system_content = '영화 후기의 감정을 분석합니다. "긍정", "중립", "부정" 중 하나로 답변하세요.'
    # 5. ChatGPT API 요청, 응답 변수 생성
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_content},
            {'role': 'user', 'content': user_content},
        ]
    )

    # 6. 응답 메시지 출력
    print(f'후기 내용 : {user_content}')
    print(f'후기 감정 : {response.choices[0].message.content}')
