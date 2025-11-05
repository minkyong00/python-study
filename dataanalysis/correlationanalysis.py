# correlationanalysis.py
# 상관 분석

import pandas as pd

economics = pd.read_csv('./assets/economics.csv')
economics.info()

# 상관행렬
print(economics[['unemploy', 'pce']].corr()) # 실업자수, 개인소비지출

# pearson 상관계수
from scipy import stats
print(stats.pearsonr(economics['unemploy'], economics['pce']))

# 상관행렬 히트맵
mtcars = pd.read_csv('./assets/mtcars.csv')
print(mtcars.head())

# 상관행렬
car_cor = mtcars.corr()

# 소수점 두째자리 반올림
car_cor = round(car_cor, 2)

# 그래프 설정
import matplotlib.pyplot as plt
plt.rcParams.update({
    'figure.dpi': 120,
    'figure.figsize': (7.5, 5.5)
})

# 히트맵
import seaborn as sns
# annot=True:상관계수 표시, cmap:히트맵 색상맵
# sns.heatmap(car_cor, annot=True, cmap="RdBu")
# plt.show()
# 상관(정방향, 역방향)

# 대각행렬 제거용 mask만들기
import numpy as np
mask = np.zeros_like(car_cor) # 행렬의 모든 데이터를 0으로
# print(mask)

# 오른쪽 위 대각행렬을 1로 바꾸기
mask[np.triu_indices_from(mask)] = 1
# print(mask)

# mask 적용된 히트맵
# sns.heatmap(car_cor, annot=True, mask=mask, cmap='RdBu')
# plt.show()

# 빈 행, 빈 열 제거
mask_new = mask[1:, :-1] # 첫 행과 마지막 열 제거
cor_new = car_cor.iloc[1:, :-1] # 상관행렬에서 제거
# sns.heatmap(cor_new, annot=True, mask=mask_new, cmap='RdBu')
# plt.show()

# 히트맵 옵션
sns.heatmap(
    data = cor_new, # 상관행렬 
    annot=True, # 상관계수 표시 여부
    cmap='RdBu', # 컬러 맵
    mask=mask_new, # 마스크
    linewidths=.5, # 경계구분선 두께
    vmax=1, # 가장 진한 파란색으로 표시할 최대값
    vmin=-1, # 가장 진한 빨간색으로 표시할 최소값
    cbar_kws={"shrink":.5} # 범례크기
)
plt.show()

























