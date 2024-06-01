# section13.py
# ChatGPT API 언어 번역기 실습 Ver1

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI
# 2. API 키 변수 생성
api_key = "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"
# 3. ChatGPT 연동
client = OpenAI(api_key=api_key)
# 4. 번역할 언어 2개 입력 받기
print("진행 순서 : 원문 언어 입력 > 번역 언어 입력 > 번역 내용 입력")
# lang1, lang2 = input().split()
# lang = input("원문의 언어를 입력해주세요(예시 한글을 영어로) : ")

lang1 = input("원문의 언어를 입력해주세요 : ")
lang2 = input("번역할 언어를 입력해주세요 : ")
# 5.사용자 메시지 입력
user_content = input("번역하고자 하는 내용을 입력해주세요 : ")
# 6. ChatGPT API 요청, 응답 변수 생성
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": lang1 + "를 " + lang2 + "로 번역해줘" },
        {"role": "user", "content": user_content},
    ]
)

# 7. 응답 메시지 출력
print(response.choices[0].message.content)