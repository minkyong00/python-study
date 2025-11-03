# objectdata
# 객체 데이터
# 객체 기반 언어라 보는게 맞음

# Pickle
import pickle
obj = { # 딕셔너리
    'name': '홍길동',
    'age': 20
}

# 딕셔너리를 obj.obj라는 바이너리 파일에 저장
with open('obj.obj', 'wb') as f:
    pickle.dump(obj, f)

# obj.obj라는 바이너리 파일 내용을 화면에 출력
with open('obj.obj', 'rb') as f:
    print(pickle.load(f))

# shelve
import shelve

# shelve.dat 파일에 키와 값을 저장
def save(key, value):
    with shelve.open('shelve') as f:
        f[key] = value

# shelve.dat 파일내의 키에 해당하는 값을 획득
def get(key):
    with shelve.open('shelve') as f:
        return f[key]

save('number', [1, 2, 3, 4, 5])
save('string', ['a', 'b', 'c'])
print(get('number'))
print(get('string'))


























