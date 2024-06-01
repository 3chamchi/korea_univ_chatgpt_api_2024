# section12.py
# ChatGPT API 언어 번역기 실습 Ver1

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI
# 2. API 키 변수 생성
# api_key = "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"
# 3. ChatGPT 연동
client = OpenAI(api_key="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")
# 4.사용자 메시지 입력
user_content = input("메시지 ChatGPT : ")
# 5. ChatGPT API 요청, 응답 변수 생성
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "한글을 입력하면 영어로 번역해줘"},
        {"role": "user", "content": user_content},
    ]
)
# 6. 응답 메시지 출력
print(response.choices[0].message.content)