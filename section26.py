# section26
# 오디오 변환기(오디오 > 텍스트)
from pathlib import Path

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

file_name = input('저장할 파일이름을 입력해주세요 : ')
# 4. 오디오로 변환할 내용 입력
file_path = Path(__file__).parent / f"{file_name}.mp3"
speech_file = open(file_path, 'rb')

# 5. ChatGPT API 요청, 응답 변수 생성
# response = client.audio.transcriptions.create(  # 언어 그대로
response = client.audio.translations.create(  # 영어로
    file=speech_file,
    model='whisper-1'
)

# 6. 응답 내용 출력
print(response.text)
