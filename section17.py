# section17.py
# ChatGPT API Chat API 메시지 연속성 실습

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = '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'

# 3. ChatGPT 연동
client = OpenAI(api_key=api_key)

# 여러 메시지를 입력 받을 변수 선언
messages_list = list()

while (True):
    # 4. 사용자 content 입력
    new_content = input('메시지를 입력해주세요 (q를 입력하면 종료됩니다): ')
    if new_content == 'q':
        break

    print('- 사용자 : ' + new_content)

    # 사용자 content 추가
    messages_list.append({'role': 'user', 'content': new_content})

    # 5. Chat API 요청
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages_list
    )
    print('- ChatGPT : ' + response.choices[0].message.content)

    # 6. 기존 메시지와 새로운 연결
    messages_list.append({'role': 'assistant', 'content': response.choices[0].message.content})

# 7. 메시지 출력
print('전체 메시지 출력')
print(messages_list)


# [
# 1 {'role': 'user', 'content': '안녕하세요~ 즐거운 수요일인가요?'},
# 2 {'role': 'assistant', 'content': '안녕하세요~ 즐거운 수요일인가요?'},
# 3 {'role': 'user', 'content': '오늘은 어떤날이셨나요?'},
# 4 {'role': 'assistant', 'content': '오늘은 어떤날이셨나요?'},
# 5 {'role': 'user', 'content': '지친하루의 힐링을 받고싶습니다'},
# 6 {'role': 'assistant', 'content': '지친하루의 힐링을 받고싶습니다'}
# ]

# [
# 1 {'role': 'user', 'content': '끝말잊기 게임하자'},
# 2 {'role': 'assistant', 'content': '기억력'},
# 3 {'role': 'user', 'content': '역도'},
# 4 {'role': 'assistant', 'content': '도전'},
# 5 {'role': 'user', 'content': '전투기'},
# 6 {'role': 'assistant', 'content': '기차'}
# ]
