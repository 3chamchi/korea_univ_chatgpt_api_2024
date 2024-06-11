# section18
# 상품 설명서 제작기 실습

# 1. ChatGPT API 패키지 불러오기
from openai import OpenAI

# 2. API 키 변수 생성
api_key = ''

# 3. ChatGPT 연동
client = OpenAI(api_key=api_key)

# 4. 상품 설명서 작성을 위한 사용자 메시지 입력받기
# 상품 장점, 타 제품과의 비교, A/S 관련
# 상품명, 주요 고객, 상품에 대한 주요 설명, 강조 키워드
# user_text1 = input('상품 설명을 위한 내용 : ')
# 입력 내용에 가이드 제공
user_text1 = input('상품명 : ')
user_text2 = input('주요 고객 : ')
user_text3 = input('주요 설명 : ')
user_text4 = input('강조 키워드 : ')

# 5. 상품 설명서 작성을 위한 시스템 메시지 작성
system_text = '''
당신은 상품 설명서를 작성하는 역할이며 설명서 작성의 전문가 입니다. 
다음 내용을 참고하여 상품 설명서를 작성해야 합니다.
답변은 두가지 버전으로 해주세요.'''

# 6. ChatGPT API 요청
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': system_text},
        # 최대한 쉬운 문법
        # {'role': 'user', 'content': '1. 상품명 : ' + user_text1 + ', 2. 주요 고객 : ' + user_text2 + ', 3. 주요 설명 : ' + user_text3 + ', 4. 강조 키워드 : ' + user_text4},
        # 편리한 문법
        {'role': 'user', 'content': f'''
        1. 상품명 : {user_text1}
        2. 주요 고객 : {user_text2}
        3. 주요 설명 : {user_text3}
        4. 강조 키워드 : {user_text4}'''},
    ]
)

# 7. ChatGPT API 응답 출력
print(response.choices[0].message.content)
