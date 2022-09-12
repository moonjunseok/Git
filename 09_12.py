# 폰트 d2coding 으로 설정 완료
# 주석 색깔 변경 완료

# p80
# 리스트 컴프리헨션
print([n * 2 for n in range(1, 10+1) if n % 2 == 1])

a = []
for n in range(1, 10+1):
    if n % 2 == 1:
        a.append(n * 2)

a

# 리스트 외에도 딕셔너리 등이 가능하다

a = {}
for key, value in original.items():
    a[key] = value

# original 은 왜 있는거지

# 제너레이터
# 루프의 반복 동작을 제어할 수 있는 루틴 형태

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
# yield 구문을 사용하면 제너레이터를 리턴할 수 있다.
# 중간 값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.

get_natural_number()

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))
# 다음값을 생성하려면 next()로 추출하면 된다.

# 제너레이트는 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능하다.
def generator():
    yield 1
    yield 'string'
    yield True
g = generator()
g
next(g)

# 제너레이트 보다는 range함수가 메모리 점유율일 훨씬 적다.

#enumerate
# '열거하다' 는 뜻의 함수
# 여러가지 자료형(list, set, tuple등)을 인덱스를 포함한 enumerate 객체로 리턴한다.
a = [1,2,3,2,45,2,5]
list(enumerate(a))

a = ['a1','a2','a3']
for i, v in enumerate(a):
    print(i, v)

# 몫과 나머지를 동시에 구하려면 divmod()함수
divmod(5, 3)

# print함수
print('a','b') # print함수는 , 를 한 칸 공백이 디폴트로 설정

print('a','b',sep =',') # sep 파라미터로 구분자를 콤마(,)로 지정