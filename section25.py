# section25
# 오디오 변환기(텍스트 > 오디오)
from pathlib import Path

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT API 연동
client = OpenAI(api_key=api_key)

# 4. 오디오로 변환할 내용 입력
input_text = input('생성할 오디오 내용을 입력해주세요 : ')

# 5. ChatGPT API 요청, 응답 변수 생성
response = client.audio.speech.create(
    model='tts-1',
    input=input_text,
    voice='onyx',
)

# 6. 음성파일 저장 위치 지정
speech_file_path = Path(__file__).parent / "speech.mp3"

# 7. 생성된 내용(바이너리 형태) 파일로 저장
# * 오디오의 경우 파일이 아닌 바이너리 형태로 응답을 받으므로 파일로 저장하는 과정이 필요
with open(speech_file_path, 'wb') as file:
    file.write(response.content)

# print(f'response.content : {response.content}')  # 확인용 바이너리 출력
print(f'\n오디오 파일이 생성되었습니다. 경로 {speech_file_path}')
