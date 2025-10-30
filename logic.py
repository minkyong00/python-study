# logic.py
# 분기문, 반복문

def p(value):
    print(value, '\n')

a = 10
if a>5:
    p("a는 5보다 큽니다!")
else:
    p("a는 5보다 크지 않습니다!")

a = 3
if a>10:
    p('a는 10보다 큽니다')
elif a>5:
    p('a는 5보다 큽니다')
else:
    p('a는 5보다 크지 않습니다')

# for
for i in [1, 2, 3, 4, 5]: # 리스트 요소 반복
    print(i, end=' ')

p('')

for str in 'Hello': # 문자열 문자 반복
    print(str, end=' ')

p('')

for i in range(1, 10): # 1~10 전까지 1씩 증가하면서 반복
    print(i, end=' ')

p('')

for i in range(1, 101, 2): # 1~101 전까지 2씩 증가하면서 반복
    print(i, end=' ')

p('')

# 중첩 for
for i in range(2, 10): # 2~9 반복
    for j in range(1, 10): # 1~9 반복
        print(f'{i}*{j}={i*j}', end=' ')
    print()

# 딕셔너리 반복
dic = {
    'a': 1,
    'b': 2,
    'c': 3
}
for i in dic.keys():
    p(i)

for i in dic.values():
    p(i)

for i in dic.items():
    p(i)

# continue : 다음번 반복 수행
# break : 가장 가까운 반복문 탈출
nums = [i for i in range(1, 11)]
for i in nums:
    if i%2==0:
        continue
    if i==9:
        break
    else:
        p(i)

# while
a = 0
while a<10:
    p(a)
    a = a + 1

a = 0
while a<10:
    if a==5:
        break
    p(a)
    a = a + 1

























