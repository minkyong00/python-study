# module&package.py
# 모듈은 관련된 변수와 함수들을 모아 놓은 파일
# 패키지는 관련된 모듈들을 포함하고 있는 폴더

# 모듈 임포트
# as : 별칭(alias)
import calc.calc as c

print(c.add(3, 5))

# 모듈내의 함수 임포트
from calc.calc import add
print(add(3, 5))
































