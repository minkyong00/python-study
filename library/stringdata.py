# stringdata.py
# 문자열 데이터 처리 라이브러리

import textwrap

str = 'Hello Python!'

# 문자열 길이 축약
print(textwrap.shorten(str, width=10, placeholder='...'))

# 문자열 공백문자 기준으로 리스트로 변환
wrapstr = textwrap.wrap(str, width=11)
print(wrapstr)

# 줄바꿈 문자를 포함해서 리스트의 요소들을 문자열로 병합
print('\n'.join(wrapstr))

# re (Reqular Expression): 정규표현식
import re

str = '홍길동의 전화번호는 010-1234-5678'
pattern = re.compile('(\d{3})-(\d{4})-(\d{4})') # 패턴
print(pattern.sub(r'(\g<1>)\g<2>-\g<3>', str))

text = 'I like apple pie' # 검색결과 리스트 반환
result = re.findall(r'apple', text)
print(result)
result = re.findall(r'p', text)
print(result)

text = 'My phone number is 010-1234-5678'
result = re.findall(r'(\d+)', text)
print(result)

# 영문대문자 검색
text = 'Hello Python'
result = re.findall(r'[A-Z]', text)
print(result)

# 영문소문자 1개이상 검색
result = re.findall(r'[a-z]+', text)
print(result)

# 문자열내의 불필요한 공백 제거
text = 'Hello       Python     This is    me'
result = re.sub(r'\s+', ' ', text)
print(result)

# 문자열 시작과 끝 검색
text = 'Hello World'
result = re.findall(r'^Hello|World$', text)
print(result)

# 날짜형식 검색
text = '오늘은 2025-01-18일 이고 내일은 2025-01-19일 입니다'
# 숫자4개-숫자2개-숫자2개
result = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(result)

text = '오늘은 2025-1-18일 이고 내일은 2025-01-19일 입니다'
# 숫자4개-숫자1개 또는 숫자2개-숫자2개
result = re.findall(r'\d{4}-\d{1,2}-\d{2}', text)
print(result)

# 문자열에서 URL 검색
text = '홈페이지 주소는 http://myhome.com 또는 http://www.myhome.com'
result = re.findall(r'http://[^\s]+', text)
print(result)

# 실습 1
# 주민등록번호 패턴
# 숫자6개-숫자7, 뒷숫자 맨 앞자리는 1~4 중 하나
text = '990101-1234567 990202-4234567'
result = re.findall(r'\d{6}-[1-4]\d{6}', text)
print(result)

# 실습 2
# 이메일 패턴
# 영문또는숫자가3~12개@영문또는숫자가3~12개.com또는.kr또는.co.kr
text = 'abc123@mycompany.com abc123@mycompany.co.kr'
result = re.findall(r'[a-zA-Z0-9]{3,12}@[a-zA-Z0-9]{3,12}\.(com|\.kr|co\.kr)', text)
print(result)

















