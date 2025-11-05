# t-test.py
# t-test (t-검정)
# 두 변수(=두 데이터군)의 평균을 기준으로 유사도를 검증하는 통계분석 기법
# scipy 외부라이브러리 사용

import pandas as pd
mpg = pd.read_csv('./assets/mpg.csv')
# mpg.info()

# category 그룹핑
# 카테고리가 compact 또는 suv인 데이터들을 category별로 그룹핑한 후
# n변수에 category에 속한 데이터의 수를
# mean변수에는 카테고리에 속한 데이터들의 도시연비의 평균을 저장
mpg_agg = mpg.query("category in ['compact', 'suv']") \
    .groupby('category', as_index=False) \
    .agg(n=('category', 'count'), mean=('cty', 'mean'))
# print(mpg_agg)

# category별 도시연비 분리
compact = mpg.query("category=='compact'")['cty']
suv = mpg.query("category=='suv'")['cty']
# print(compact, suv)

# t-test
from scipy import stats
# states.ttest_ind: 두 데이터군의 유사도 검증 함수
# equal_var=True : 데이터의 분산이 같다고 가정
# TtestResult(statistic=np.float64(11.917282584324107), pvalue=np.float64(2.3909550904711282e-21), df=np.float64(107.0))
# 카테고리별 구분한것이 도시연비에 영향을 줌 -> 우연히 발생할 확률이 적음 -> 필연적 발생 -> 상관이 있음

# p-value가 0.05이하이면
#  차이가 우연히 발생할 확률이 적다 
#   = 두 데이터군의 값의 차이가 유의미함
#   = 서로 상관이 있음
#   => 카테고리마다 도시연비의 차이가 발생할 확률이 높다
#   => 카테고리가 뭐냐에 따라 도시연비의 차이가 발생함
# print(stats.ttest_ind(compact, suv, equal_var=True))

# t-test 실습
# 일반휘발유(fl이 r)와 고급휘발유(fl이 p)의 도시연비(cty) 차이에 대한 유사도 분석
# mpg.info()
mpg_fl = mpg.query("fl in ['r', 'p']") \
    .groupby('fl', as_index=False) \
    .agg(n=('fl', 'count'), mean=('cty', 'mean'))
# print(mpg_fl)

r = mpg.query("fl == 'r'")['cty']
p = mpg.query("fl == 'p'")['cty']
# print(r, p)

print(stats.ttest_ind(r, p, equal_var=True))
# pvalue=np.float64(0.28752051088667036)
# 0.05보다 크므로
# 일반/고급 휘발유를 넣는것이 도시연비에는 영향이 없다
























