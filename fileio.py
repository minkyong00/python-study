# fileio.py
# 파일 입출력

# 키보드 입력 받아 문자열 저장
# str = input("문자열을 입력해주세요!")
# print(f"입력하신 문자열은 {str} 입니다")

# 키보드로 입력받은 두 수의 합 출력
# num1 = int(input('첫번째 숫자 입력'))
# num2 = int(input('두번째 숫자 입력'))
# print(f'두 수의 합: {num1 + num2}')

# file io

# f = open('datafile.txt', 'w', encoding='UTF-8') # 쓰기모드로 파일 열기
# f.write('Hello Python!\n')
# f.write('안녕 파이썬!\n')
# f.close()

# f = open('datafile.txt', 'r', encoding='UTF-8')
# print(f.readline()) # 한 줄 읽어서 문자열 반환
# print(f.read()) # 전체를 읽어서 문자열 반환
# print(f.readlines()) # 각 줄 문자열들의 리스트 반환
# f.close()

#  JSON 읽고 쓰기
# jsonStr = '{"name": "홍길동", "age": 25, "city": "New York"}\n'
# f = open('test.json', 'w', encoding='utf-8')
# f.writelines([jsonStr, jsonStr]) # 리스트내의 문자열들을 각 라인으로 쓰기, 여러개는 리스트
# f.close()

# f = open('test.json', 'r', encoding='utf-8')
# print(f.read())
# f.close()
























