# section15.py
# 번역, 이미지 생성 응용 실습

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
    model='dall-e-3',
    prompt=prompt,
)

# 8. 생성된 이미지 출력
print(image_response.data)
