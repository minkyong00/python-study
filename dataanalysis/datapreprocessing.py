# datapreprocessing.py
# 데이터 전처리

import pandas as pd

df = pd.DataFrame({
    'name': ['kim', 'lee', 'park', 'choi', 'hong'],
    'nclass': [1, 1, 2, 2, 2],
    'kor': [10, 20, 30, 40, 50],
    'eng': [30, 40, 50, 60, 70],
    'math': [50, 60, 70, 80, 90]
})
print(df.shape)

# 조건에 맞는 행 추출
print(df.query('kor==10'))
print(df.query('kor!=10'))
print(df.query('eng>50'))
print(df.query('nclass==1 & eng>=40'))
print(df.query('nclass==1 | eng>=40'))
print(df.query('kor in [10, 30, 50]'))

# 변수를 조건에 사용
korList = [10, 30, 50]
print(df.query('kor in @korList'))

# 특정 변수(들) 추출
print(df['kor'])
print(type(df['kor'])) #Series
print(df[['eng', 'math']])
print(type(df[['eng', 'math']])) #DataFrame

# 변수 제거
print(df.drop(columns='math'))
print(df.drop(columns=['kor', 'eng']))
print(df) # 저장하지 않으면 원본
df = df.drop(columns=['math', 'eng'])
print(df)

# 함수 조합
print(df.query('nclass==2')['kor'])
print(df.query('nclass==2')['kor'].head(2))

# 변수 추가 시 조건 부여
import numpy as np
resultdf = df.assign(result = np.where(df['kor']>=20, 'pass', 'fail'))
# df['result'] = np.where(df['kor']>=20, 'pass', 'fail')
print(resultdf)

# 그룹핑
print(df.agg(mean_kor=('kor', 'mean'))) # 집계함수, 국어 평균

# 반별로 그룹핑한 후 국어 평균
print(df.groupby('nclass').agg(mean_kor=('kor', 'mean'))) 

# 그룹별 여러 통계
print(
    df.groupby('nclass').agg(
        mean_kor= ('kor', 'mean'), # 반별 국어 평균
        sum_kor= ('kor', 'sum'), # 반별 국어 합계
        median_kor= ('kor', 'median'), # 반별 국어 중간값(50%)
        count_kor= ('kor', 'count'), # 반별 국어점수 개수
    )
)

# 데이터 합치기

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'mid': [100, 90, 80]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'final': [90, 80, 70]
})

# 행 합치기
print(pd.concat([df1, df2]))

# 변수(열) 합치기
print(pd.merge(df1, df2, on='id')) # on: 기준 변수
print(pd.merge(df2, df1, on='id')) # on: 기준 변수






















