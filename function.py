# function.py
# 사용자 정의 함수

# 함수 선언
'''
def 함수명(파라미터리스트):
    코드블럭..
    return 리턴값
'''

def add(a, b):
    return a + b

print(add(5, 6))

print(add('hello', ' python'))

# print(add()) # TypeError
# print(add(3)) # a+b연산을 해야 하는데 한쪽이 None > None은 연산 불가 > TypeError
# print(add(1, 2, 3))

# 파라미터 기본 값
def multi(a, b=3):
    return a * b
print(multi(5, 3))
print(multi(5))

# 람다 함수
# 함수 문법을 간소화시킨 형태의 함수
# 파이썬에서 함수는 리터럴이므로 다른 함수에 인자로 전달이 가능
lambda_add = lambda a, b: a + b
print(lambda_add(5, 6))

def calc(a, b, func):
    return func(a, b)

func1 = lambda a, b: a + b
print(calc(1, 2, func1))

func2 = lambda a, b: a * b
print(calc(1, 2, func2))

# 즉시 실행 함수
print((lambda a=1, b=2: a * b)())






















