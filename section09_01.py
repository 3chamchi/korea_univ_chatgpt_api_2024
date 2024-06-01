from openai import OpenAI

client = OpenAI(
    api_key='sk-proj-5DGQEXHFaQHWME4RjWJaT3BlbkFJv9jYDOeaZi6V9FysVK4E',
)

print(f"===== 번역기 Ver1 =====")
print(f"* 번역 언어 : 한국어 -> 영어")
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
