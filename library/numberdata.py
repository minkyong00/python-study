# numberdata.py
# 숫자데이터 처리 라이브러리

# math : 수학 관련 라이브러리
import math
import statistics

print(math.gcd(60, 80, 100)) # 최대공약수
print(math.lcm(15, 25)) # 최소공배수

# decimal : 소수 관련 라이브러리
from decimal import Decimal
print(0.1 * 3)
print(Decimal('0.1') * 3)

# fractions: 분수 관련 라이브러리
from fractions import Fraction
print(Fraction(1.5))

# random: 랜덤 수 관련 라이브러리
import random
print(random.random()) # 0.0 보다 크거나 같고 1.0보다 작은 임의의 실수
print(random.randint(1, 45)) # 1~45 중 임의의 정수

# 로또 숫자 6개 추출
number = []
for i in range(6):
    number.append(random.randint(1, 45))
print(number)

lottoNum = set()
while True:
    lottoNum.add(random.randint(1, 45))
    if len(lottoNum) == 6:
        break
print(list(lottoNum))

# statistice : 기초 통계 (평균값, 표준편차, 분산, 25%, 50%(중앙값), 75%, 최대, 최소...)
import statistics as stat
score = [38, 54, 45, 87, 99, 100, 25, 32, 44, 16]
print(stat.mean(score)) # 평균
print(stat.median(score)) # 중앙값
print(stat.stdev(score)) # 표준편차
print(stat.variance(score)) # 분산
qt = stat.quantiles(score) # 4분위 수, 리스트 반환
print(qt[0]) # 25%
print(qt[1]) # 50%
print(qt[2]) # 75%



































