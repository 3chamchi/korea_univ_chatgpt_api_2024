# section27
# 끝말잇기 게임

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

messages = [
    {'role': 'system', 'content': '당신은 끝말잇기 게임 상대입니다. 끝말잇기 게임 시작'},
]
print('끝말잇지 시작!')
while True:
    user_text = input('나 : ')
    messages.append({'role': 'user', 'content': user_text})

    # 5. ChatGPT API 요청, 응답 변수 생성
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    messages.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})

    if len(messages) > 5:
        messages.pop(1)
        messages.pop(2)

    # 6. 응답 내용 출력
    print(f'상대 : {response.choices[0].message.content}')
