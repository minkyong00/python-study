# dataanalysis.py
# DataFrame 분석

import pandas as pd

exam = pd.read_csv('assets/exam3.csv')
print(exam)

print(exam.head()) # 상위 5개행
print(exam.head(10)) # 상위 10개행

print(exam.tail()) # 하위 5개행
print(exam.tail(10)) # 하위 10개행

print(exam.shape) # 행/열 수 튜플, 데이터의 차원  

exam.info() # 데이터프레임 구조

# 기초통계: 개수, 평균, 표준편차, 최소, 25%, 50%, 75%, 최대
print(exam.describe())
print(type(exam.describe()))
print(exam['kor'].describe())
print(type(exam['kor'].describe()))

# DataFrame 생성
df_org = pd.DataFrame({
    'var1': [1, 2, 1],
    'var2': [2, 3, 2]
})
print(df_org)

# 변수명 변경
df_new = df_org.rename(columns={'var1':'data1'})
print(df_new)

# 변수 생성
df_new['data2'] = df_new['data1'] + df_new['var2']
print(df_new)

# 그래프 라이브러리
# matplotlib 외부라이브러리 필요

df_score = pd.DataFrame({
    'name': ['홍길동', '강감찬', '이순신'],
    'kor': [90, 80, 70],
    'eng': [100, 90, 80],
    'math': [60, 50, 40]
})

import matplotlib.pyplot as plt
# 박스플랏은 데이터 분포에 대한 그래프(최소, 최대, 25, 50, 75)
df_score.boxplot(column=['kor', 'eng', 'math']) # 3개 컬럼에 대한 박스플랏
#plt.show() # 그래프 화면에 출력

# numpy를 활용한 조건 부여
# numpy는 데이터의 수치 계산, 조건처리, 배열 처리 등에 많이 활용되는 외부라이브러리
import numpy as np
df_score['test'] = np.where(df_score['math']>=60, 'pass', 'fail')
print(df_score)

# 값으로 그룹핑했을 때 각각의 개수 출력
counts = df_score['test'].value_counts()
print(counts)

# 조건 중첩
df_score['grade'] = np.where(df_score['math']>=60, 'A',
                        np.where(df_score['math']>=50, 'B', 'C'))
print(df_score)

# 수학점수에 따른 오름차순 정렬
df_score_sorted = df_score['math'].sort_values()
print(df_score_sorted)

# 수학점수에 따른 내림차순 정렬
df_score_sorted = df_score['math'].sort_values(ascending=False)
print(df_score_sorted)












