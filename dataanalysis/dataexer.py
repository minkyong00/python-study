# dataexer.py
# 실습

# 아래 순서대로 실습을 해봅시다!
# 1. https://jsonplaceholder.typicode.com/todos JSON데이터를 호출해 DataFrame을 생성
# 2. userId가 5이상 인것들을 추출
# 3. userId 역순으로 정렬
# 4. 결과를 result.csv로 저장

import pandas as pd
import requests
import json

# 1
response = requests.get('https://jsonplaceholder.typicode.com/todos')
todosJson = response.json()
todosDF = pd.DataFrame(todosJson)
print(todosDF)

# 2
subDF = todosDF.query("userId>=5")
print(subDF)

# 3
sortedDF = subDF.sort_values("userId", ascending=False)
print(sortedDF)

# 4
sortedDF.to_csv("assets/result.csv")