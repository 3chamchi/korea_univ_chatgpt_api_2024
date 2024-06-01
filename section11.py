# section11.py
# ChatGPT API 연동 - 입력 문구 입력 받기

# 1. ChatGPT 연결을 위한 패키지 불러오기
from openai import OpenAI
# 2. ChatGPT API 키 변수 생성, 키 값 지정
api_key = ""
# 3. ChatGPT 연동
client = OpenAI(
    api_key=api_key
)
# 4. 사용자 메시지 입력 받기
user_content = input()
# 5. ChatGPT API 요청
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[  # role : system or user
        {"role": "user", "content": user_content},
    ]
)
# 6. ChatGPT API 응답 출력
print(response.choices[0].message.content)
