# dataTypes
# 파이썬의 데이터 타입



# 출력용 함수
def p(value):
    print(value, '\n')

# number
p(1) # 정수
p(0.1) # 실수
p(3E5) # 3 곱하기 10의 5승(exponential)
p(0o10) # 8진수 10
p(0xFF) # 16진수 FF
p(1+2) # 숫자 덧셈
p(3**3) # 3의 3승
p(7%4) # 7을 4로 나눈 나머지
p(7//4) # 7을 4로 나눈 몫

# string
p("hello")
p('hello')
# 여러 줄 문자열
p('''
이것은
여러 줄 문자열
입니다
''')
'''
이것은
여러 줄 주석
입니다
'''
#따옴표 중첩
p("Hello 'Tom'")
p('Hello "Tom"')
p("Hello\nTom") # 줄바꿈 문자
p('Hello' + 'Tom') # 문자열 접합
p('Hello'*3) #문자열 반복
p(len('Hello')) # 문자열 길이 (문자의 수)

str = "Hello There"
p(type(str)) # <class 'str'>
p(str[0]) # 인덱스 0의 문자
p(str[:3]) # 인덱스 0~2의 문자
p(str[3:]) # 인덱스 3부터 끝까지 문자
p(str[3:5]) # 인덱스 3부터 4까지 문자
p(str[::2]) # 인덱스 0부터 끝까지, 스텝2

# 파이썬은 자바스크립트처럼 인터프리터 언어
# 파이썬은 동적타이핑(변수에 할당하는 리터럴의 타입이 변수의 타입을 결정)을 사용
str = "Hello"
p(type(str)) # <class 'str'>
str = 100
p(type(str)) # <class 'int'>
str = 3.14
p(type(str)) # <class 'float'>
# 포맷팅 프린트
str = 'Jane'
age = 20
p("%s은 %d살입니다!" %(str, age))
p(f"{str}은 {age}살입니다!")

# 문자열 처리 함수
str = "hello there"
p(str.count('e')) # e문자의 개수
p(str.find('e')) # e문자가 처음 나온 곳의 인덱스
p(str.find('p')) # 문자가 없으면 -1 반환
p(str.upper()) # 대문자로
p(str.lower()) # 소문자로
p(str.replace('e', 'k')) # 문자 대체
p(str.split()) # 문자열을 공백문자 기준으로 리스트로 변환
p(str.split('e')) # 문자열을 e문자 기준으로 리스트로 변환
p('010-1234-5678'.split('-'))

# list : []
even = [2, 4, 6, 8] # length:4, index:0~3
odd = [1, 3, 5, 7] # length:4, index:0~3

print(even, odd)

p(even[0])
p(even[0:])
p(even[:2]) # 인덱스 0~1
p(even[::2])
p(even[-1]) # 뒤에서 첫번째

p(even + odd) # 리스트 변합
p(even*3) # 리스트 요소 반복
p(even.index(6)) # 6요소가 처음 나온 곳의 인덱스
p(len(even))

del even[0] # 인덱스 0의 요소 제거
p(even)

even.append(10) # 리스트 맨 뒤에 10 추가
p(even)

even.reverse() # 리스트 요소 순서 180도 반전
p(even)

even.sort() # 오름차순
p(even)

even.insert(0, 2) # 0번 인덱스에 2 추가
p(even)

even.remove(2)
p(even)

even.pop() # 리스트 맨 뒤 요소 제거
p(even)

even.extend([10, 12]) # 리스트의 요소들을 기존 리스트에 추가
p(even)

even.append([10, 12]) # 리스트 맨 뒤에 [10, 12] 요소를 추가
p(even)

# tuple : ()
# 리스트와 사용법이 동일하지만 요소 추가/삭제/변경 불가

yoil = ('월', '화', '수', '목', '금', '토', '일')
p(yoil)

# dictionary : {}
# 딕셔너리는 아이템(키:값)들의 집합
dic = {
    'name': '홍길동',
    'age': 20,
    'address': '서울'
}
p(dic)

dic['gender'] = '여' # 아이템 추가
p(dic)

del dic['gender'] # 아이템 제거
p(dic)

# 딕셔너리 함수
p(dic.keys()) # 키들을 추출해서 dict_keys를 반환
p(list(dic.keys())) # 키들의 리스트
p(dic.values()) # 값들을 추출해서 dict_values를 반환
p(list(dic.values())) # 값들의 리스트
p(dic.items()) #아이템들을 추출해서 dict_items를 반환
p(list(dic.items())) # 아이템들의 리스트

p('name' in dic) # 딕셔너리에 name키가 있는지
p('gender' in dic) # 딕셔너리에 gender키가 있는지

# set : {}
# 중복요소를 하나만 저장

s = {1, 2, 3, 4, 5, 1, 2, 3}
p(s)

s = set([1, 2, 3, 4, 5, 1, 2, 3]) # 리스트를 셋으로, 리스트 중복요소 제거
p(s)

l = list(s) # 셋을 리스트로
p(l)

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
p(s1 & s2) # 교집합
p(s1 | s2) # 합집합
p(s1 - s2) # 차집합(s1에만 있는 요소들)
p(s2 - s1) # 차집합(s2에만 있는 요소들)

# boolean
# True, False
# 문자열에 문자가 1개이상 있으면 True
# 리스트, 튜플, 셋에 요소가 1개 이상있으면 True
# 딕셔너리에 아이템이 1개 이상 있으면 True
# 숫자인 경우 0은 False, 0이 아니면 True
# None은 False (None은 값이 정해지지 않음을 뜻하는 값)

p(1==1) #T
p(2<1) #F
p(bool('hello')) #T
p(bool('')) #F
p(bool([1, 2, 3])) #T
p(bool([])) #F
p(bool({'name':'홍길동'})) #T
p(bool({})) #F
p(bool(0)) #F
p(bool(100)) #T















