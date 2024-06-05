# section16.py
# 번역, 이미지 생성 응용 실습 - 심화 한글 프롬프트와 영문 프롬프트 비교

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT 연동
client = OpenAI(api_key=api_key)

# 4. 이미지 생성할 내용 입력 받기
# 출력 : print()
# 입력 : input()
user_content = input("생성하고자하는 이미지를 설명해주세요 : ")
print(user_content)
# 5. 입력 받은 내용 번역 요청
chat_response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': "system", 'content': '입력한 내용을 영어로 번역해줘'},
        {'role': "user", 'content': user_content},
    ]
)

# 6. 번역된 내용 출력
print(chat_response.choices[0].message.content)
prompt = chat_response.choices[0].message.content

# 7. 번역된 내용 이미지 생성 요청
image_response = client.images.generate(
    model='dall-e-2',
    prompt=prompt,
)

# 8. 생성된 이미지 출력
print('번역하여 이미지 생성')
print(image_response.data)

# 9. 원문 내용 이미지 생성 요청
image_response2 = client.images.generate(
    model='dall-e-2',
    prompt=user_content,
)

# 10. 생성된 이미지 출력
print('원문으로 이미지 생성')
print(image_response2.data)
