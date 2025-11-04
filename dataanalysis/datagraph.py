# datagraph.py
# seaborn을 활용한 그래프

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('./assets/mpg.csv')

# 산점도
# sns.scatterplot(data=mpg, x='displ', y='hwy')
# plt.show()

# 축 범위 설정
# sns.scatterplot(data=mpg, x='displ', y='hwy').set(xlim=[3, 6])
# plt.show()

# sns.scatterplot(data=mpg, x='displ', y='hwy').set(xlim=[3, 6], ylim=[10, 30])
# plt.show()

# 종류별 색상 변경: hue 범례
# sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
# plt.show()

# 그래프 설정
plt.rcParams.update({'figure.dpi': '150'}) # 해상도, 기본값 72
plt.rcParams.update({'figure.figsize': [8, 6]}) # 크기(인치), 기본값 [6, 4]
plt.rcParams.update({'font.size': '8'}) # 글자크기, 기본값 10
plt.rcParams.update({'font.family': 'Malgun Gothic'}) # 글자체, 기본값 sans-serif
# sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
# plt.show()

# 막대그래프
df_mpg = mpg.groupby('drv').agg(mean_hwy=('hwy', 'mean'))
print(df_mpg)

# sns.barplot(data=df_mpg, x='drv', y='mean_hwy')
# plt.show()

# 막대 크기순 정렬
# df_mpg = df_mpg.sort_values('mean_hwy', ascending=False)
# sns.barplot(data=df_mpg, x='drv', y='mean_hwy')
# plt.show()

# 빈도 막대그래프
df_mpg = mpg.groupby('drv').agg(n=('drv', 'count'))
# sns.barplot(data=df_mpg, x='drv', y='n')
# plt.show()

# sns.countplot(x='drv', data=mpg, order=['4', 'f', 'r'])
# plt.show()

# 빈도수 높은 순으로 정렬
# sns.countplot(x='drv', data=mpg, order=mpg['drv'].value_counts().index)
# plt.show()

# 라인그래프

economics = pd.read_csv('./assets/economics.csv')

# sns.lineplot(data=economics, x='date', y='unemploy')
# plt.show()

# X축에 연도 표시
economics['date2'] = pd.to_datetime(economics['date']) # 문자열 > 날짜
economics['year'] = economics['date2'].dt.year
# ci=None : 신뢰구간 표시 안함
# sns.lineplot(data=economics, x='year', y='unemploy', ci=None)
# plt.show()

# 박스그래프
sns.boxplot(data=mpg, x='drv', y='hwy', hue='year')
plt.show()



























