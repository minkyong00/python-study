# textmining2.py
# 텍스트 마이닝

import pandas as pd

df = pd.read_csv('./assets/news_comment_BTS.csv')
# df.info()

# 한글이 아닌 모든 문자 제거
import re
df['reply'] = df['reply'].str.replace('[^가-힣]', ' ', regex=True)
# print(df['reply'])

# Kkma 형태소 분석기를 통해 명사 추출
import konlpy
kkma = konlpy.tag.Kkma()
nouns = df['reply'].apply(kkma.nouns)
# print(nouns)

# 리스트 분해
nouns = nouns.explode()
# print(nouns)

# 데이터프레임 생성
df_word = pd.DataFrame({'word': nouns})

# 글자 수 컬럼 추가
df_word['count'] = df_word['word'].str.len()
# print(df_word)

# 두 글자 이상 단어 추출
df_word = df_word.query('count>=2.0')
# print(df_word)

# 단어별 빈도
# word의 갯수를 n에 넣음
df_word = df_word.groupby('word', as_index=False) \
    .agg(n=('word', 'count')) \
    .sort_values('n', ascending=False)
# print(df_word)

# 빈도 상위 20개 추출
top20 = df_word.head(20)
# print(top20)

# 막대그래프 그리기
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams.update({
    "font.family": "Malgun Gothic",
    "figure.dpi": "120",
    "figure.figsize": [6.5, 6]
})
sns.barplot(data=top20, y="word", x="n")
plt.show()

## 워드 클라우드 만들기

# 한글표현을 위한 폰트 설정
font = "./assets/DoHyeon-Regular.ttf"

# 데이터 프레임을 딕셔너리로 변경
dic_word = df_word.set_index("word").to_dict()["n"]
print(dic_word)

# 워드클라우드 생성
import matplotlib.pyplot as plt
from wordcloud import WordCloud
wc = WordCloud(
    random_state = 1234,    # 모양을 랜덤하게 하기 위한 난수
    font_path = font,
    width = 400,
    height = 400,
    background_color = "white"
)
img_wordcloud = wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10, 10)) # 가로,세로 크기
plt.axis("off") # 테두리 선 없애기
plt.imshow(img_wordcloud) # 이미지 보여주기
plt.show()


## 구름모양 워드 클라우드 만들기
# 이미지 로드
from PIL import Image
icon = Image.open("assets/cloud.png")

# 마스크(mask) 생성
import numpy as np
img = Image.new("RGB", icon.size, (255, 255, 255))
img.paste(icon, icon)
img = np.array(img)

# 워드클라우드 생성
wc = WordCloud(
    random_state = 1234,    # 모양을 랜덤하게 하기 위한 난수
    font_path = font,
    width = 400,
    height = 400,
    background_color = "white",
    mask = img,
    colormap="inferno" # 컬러맵 설정
)
img_wordcloud = wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10, 10)) # 가로,세로 크기
plt.axis("off") # 테두리 선 없애기
plt.imshow(img_wordcloud) # 이미지 보여주기
plt.show()

















































