# section14.py
# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = "sk-proj-vVbQsomD8Nx2NPWG91itT3BlbkFJlRigZtWnr9z06nuYyvCC"

# 3. ChatGPT 연동
client = OpenAI(api_key=api_key)

# 4. 생성할 이미지 설명 입력 받기
prompt = input("생성할 이미지의 설명을 입력해주세요 : ")

# 번역 API 사용
# 5. ChatGPT API 요청, 응답 변수 생성
response = client.images.generate(
    prompt=prompt,
    model="dall-e-3",
    # size="256x256",
)

# 6. 응답 메시지 출력
print(response.data)
