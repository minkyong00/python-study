# exceptionHandling.py
# 예외 처리

# 예외 발생
# ZeroDivisionError, 예외 처리 안하면 예외 발생시키고 로직 종료
# result = 10 / 0

# 예외 처리
# try: #예외 발생 가능한 코드 블럭
#     result = 10 / 0
# except ZeroDivisionError: # ZeroDivisionError 처리 코드 블럭
#     print("0으로 나눌 수 없음")
# finally: #예외 발생 여부와 상관없이 수행되는 코드 블럭
#     print('예외 발생과 관계없이 출력됨')

# 사용자 정의 예외
class Under19Exception(Exception):
    def __str__(self):
        return '19세 이하 관람불가!'

age = 18
if age < 19:
    try:
        # result = 10 / 0
        raise Under19Exception() # 예외를 발생 시킨
    except ZeroDivisionError:
        print('0으로 나눌 수 없음')
    except Under19Exception:
        print('19세 이하 관람불가 예외 처리!')
    finally:
        print('예외 발생과 관계없이 출력됨')











