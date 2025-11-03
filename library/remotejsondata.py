# remotejsondata.py
# 원격 json 데이터

import requests
import json

# GET 방식 요청
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())

# POST 방식 요청
sendData = {
    "userId": 1,
    "id": 101,
    "title": "sample title",
    "body": "sample body"
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=sendData)
print(response.text)

# urllib
from urllib.request import urlopen
response = urlopen('https://jsonplaceholder.typicode.com/posts')
if response.getcode() == 200:
    data = json.loads(response.read().decode('utf-8'))
    for post in data:
        print(post['title'])
else:
    print('요청 에러!')

# aiohttp
import aiohttp # 비동기 요청
import asyncio # 비동기 입출력

# 비동기 요청 메소드
async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = await fetch_json(url)
    print(json.dumps(data, indent=4)) # indent: JSON 들여쓰기 문자 개수

asyncio.run(main())




















