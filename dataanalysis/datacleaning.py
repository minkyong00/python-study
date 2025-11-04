# datacleaning.py
# 데이터 정제 (결측치, 이상치, 극단치 ..)

import pandas as pd
import numpy as np

# 결측치 생성 : np.nan
df = pd.DataFrame({
    'name': ['홍길동', '강감찬', np.nan, '이순신'],
    'score': [100, 90, 80, np.nan]
})
print(df)

# 결측치 연산 불가: NaN은 연산 불가
df['compscore'] = df['score'] - 10 # NaN - 10 => NaN
print(df)

# 결측치 확인: pd.isna
print(pd.isna(df))

# 결측치 개수(빈도) 확인
print(pd.isna(df).sum())

# 결측치 제거 : 결측치를 포함한 행 전체가 제거됨
print(df.dropna(subset=['score']))

# 전체 결측치 제거
print(df.dropna(subset=['name', 'score']))
print(df.dropna())

# 결측치 대체

# 행/열 인덱스에 해당하는 결측치 대체
print(df)
df.loc[[2], ['name']] = '유관순'
print(df)
df.loc[[3], ['score']] = 70
print(df)

# 열에 있는 모든 결측치 대체
df['compscore'] = df['compscore'].fillna(80)
print(df)


# 이상치
df2 = pd.DataFrame({
    'name': ['홍길동', '강감찬', '코리아IT'],
    'score': [100, 120, 80]
})

# 이상치 개수 확인 : 각 값의 개수 확인
print(df2['name'].value_counts())
print(df2['score'].value_counts())

# 이상치를 결측치 처리
df2['score'] = np.where(df2['score']>100, np.nan, df2['score'])
print(df2)
df2 = df2.dropna(subset=['score'])
print(df2)

# 극단치

# 극단치 확인을 위해 그래프(박스그래프)
# seaborn 외부라이브러리 필요
import seaborn as sns
import matplotlib.pyplot as plt
mpg = pd.read_csv('./assets/mpg.csv')
print(mpg)
mpg.info()
sns.boxplot(y='hwy', data=mpg)
# plt.show()

# 극단치 기준값(Q1, Q3)
pct25 = mpg['hwy'].quantile(0.25) # 1/4, 1사분위 수
pct75 = mpg['hwy'].quantile(0.75) # 3/4, 3사분위 수
print(pct25, pct75)

# IQR(Inter Quantile Range: 사분위 범위) : 3사분위 수에서 1사분위 수를 뺀 값
iqr = pct75 - pct25
print(iqr)

# 상한/하한 정하기 (사람이 정하는 것)
uplimit = pct75 + 1.5*iqr
downlimit = pct25 - 1.5*iqr
print(uplimit, downlimit)

# 정한 상한/하한 기준으로 극단치를 결측치 처리
mpg['hwy'] = np.where(
    (mpg['hwy']<downlimit) | (mpg['hwy']>uplimit),
    np.nan,
    mpg['hwy']
)
print(mpg['hwy'].value_counts())

# 결측치 빈도(개수) 확인
print(mpg['hwy'].isna().sum())

# 결측치 제거 후 drv로 그룹핑한 후 각 그룹의 고속도로 연비 평균 산출
print(mpg.dropna(subset=['hwy']).groupby('drv') \
      .agg(mean_hwy=('hwy', 'mean')))




























