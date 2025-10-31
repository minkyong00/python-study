# class&object.py
# 클래스와 객체

# 클래스 정의
class Human:
    humanCount = 0 # 클래스 변수: 객체들이 값을 공유하는 변수
    # 생성자 함수
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setName(self, name): # setter
        self.name = name
    def getName(self): # getter
        return self.name

# 객체 생성
hong = Human("홍길동", 20)
print(hong.humanCount, hong.name, hong.age)
kang = Human("강감찬", 30)
print(kang.humanCount, kang.name, kang.age)

# 클래스 변수 값 변경
Human.humanCount = 1
print(hong.humanCount, kang.humanCount)
Human.humanCount = 2
print(hong.humanCount, kang.humanCount)

# 상속 & 오버라이딩
class Vehicle:
    def __init__(self, name, tireCount):
        self.name = name
        self.tireCount = tireCount
    def getName(self):
        return f'이 탈것의 이름은 {self.name}입니다!'

# Car는 Vehicle을 상속
class Car(Vehicle):
    def getName(self):
        return f'이 차의 이름은 {self.name}입니다!'

car = Car('벤츠', 4)
print(car.name, car.tireCount)

car = Vehicle('BMW', 4)
print(car.name, car.tireCount)

# 오버라이딩
# 파이썬은 재정의가 가능하기때문에 상위껄 재정의한다는 것은 의미가 없을 수 있음
class Bird():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def cry(self):
        print(f'새는 {self.sound} 소리를 냅니다')

class Eagle(Bird):
    def cry(self):
        print(f'독수리는 {self.sound} 소리를 냅니다')
              
class Chicken(Bird):              
    def cry(self):
        print(f'닭은 {self.sound} 소리를 냅니다')


eagle = Eagle('독수리', '꽤꽤')
chicken = Chicken('닭', '꼬끼오')
eagle.cry()
chicken.cry()










