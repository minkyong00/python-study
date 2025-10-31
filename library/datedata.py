# datedata.py
# 날짜 데이터 처리 라이브러리

# datetime: 날짜/시간 관련 라이브러리
import datetime
today = datetime.date.today() # 오늘날짜
print(today)

todaytime = datetime.datetime.today() # 오늘 날짜와 시간
print(todaytime)

print(today.weekday()) # 요일(월요일이 0)

# 날짜 연산
print(today + datetime.timedelta(days=100)) # 100일 후
print(today + datetime.timedelta(days=-100)) # 100일 전
print(today + datetime.timedelta(weeks=3)) # 3주 후
print(today + datetime.timedelta(hours=45)) # 45시간 후

day1 = datetime.date(2019, 1, 1)
day2 = datetime.date(2025, 10, 31)
print(day2 - day1) # 두 날짜간 차이

# calendar
import calendar as cal
print(cal.weekday(2025, 10, 31))
print(cal.isleap(2025)) # 윤년 여부




































