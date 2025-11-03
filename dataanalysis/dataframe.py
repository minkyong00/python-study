# dataframe.py
# pandas의 DataFrame

import pandas as pd

# 딕셔너리를 가지고 DataFrame 생성
df = pd.DataFrame({
    'name': ['홍길동', '강감찬', '이순신'],
    'kor': [90, 80, 70],
    'eng': [100, 90, 80],
    'math': [60, 50, 40]
})
print(df)
print(type(df)) # DataFrame (2차원: 2차원데이터+인덱스)
# 데이터에 접근하기 위해 인덱스 필요

print(df['name'])
print(type(df['name'])) # Series (1차원: 1차원데이터+인덱스)
# series 두개 이상 있을 시 dataFrame

# kor 변수의 합 출력
print(sum(df['kor']))

# kor 변수의 평균 출력
print(sum(df['kor'])/3)

# 엑셀파일로 DataFrame 생성
# openpyxl 외부라이브러리 필요
df_xl_exam = pd.read_excel('assets/exam.xlsx')
print(df_xl_exam)

# 행(데이터 건수)의 수
print(len(df_xl_exam))

# CSV파일로 DataFrame
df_csv_exam = pd.read_csv('assets/exam.csv')
print(df_csv_exam)

# DataFrame을 CSV파일로
df.to_csv('assets/exam2.csv', index=False)

# JSON파일로 DataFrame 생성
df_json_exam = pd.read_json('assets/exam.json')
print(df_json_exam)

# DataFrame을 JSON 파일로
df.to_json('assets/exam2.json', indent=4)

# XML파일로 DataFrame 생성
# lxml 외부라이브러리 필요
de_xml_exam = pd.read_xml('assets/exam.xml')
print(de_xml_exam)

# DataFrame을 XML파일로
df.to_xml('assets/exam2.xml', index=False)











