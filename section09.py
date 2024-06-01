from openai import OpenAI

client = OpenAI(
    api_key='',
)

text = input('번역할 내용을 입력해주세요 : ')

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "한국어를 영어로 번역해줘."},
        {"role": "user", "content": text},
    ]
)
# 응답 출력
print(f"원문 : {text}")
print(f"번역 : {response.choices[0].message.content}")
