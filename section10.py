# section10.py
# ChatGPT API 연동
from openai import OpenAI

api_key = ""

client = OpenAI(
    api_key=api_key
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "안녕하세요 여기는 한국입니다!"},
    ]
)

print(response.choices[0].message.content)
