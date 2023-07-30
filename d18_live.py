import math

## 실수 다루기 
# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))

# print(5 / 3)

# a, b를 같은 수로 볼 수 있는지 판단
a = 3.2 - 3.1
b = 1.2 - 1.1
# 1
print(abs(a - b) <= 1e-10)
# 2
print(math.isclose(a, b)) 

# 지수 표현 10^
print(314e-2, 314e2) # 3.14, 31400.0

## sequence type(정렬 x)
# 문자열(불변 자료형 - 인덱스로 접근은 가능하지만 변경은 불가하다. )
# print("문자열 안에 '작은 따옴표'를 표시하는 방법")
# print("문자열 안에 \"큰 따옴표\"를 표시하는 방법")
# print("\\") # 백슬래시

# 문자열 내에 변수나 표현식 삽입
bugs = 'roaches'
counts = 13
area = 'living room'

print(f'Debugging {bugs} {counts} {area}')

# f-string 응용(advanced)
greeting = 'hi'
print(f'{greeting:^10}') # 10칸 중 가운데 정렬
print(f'{greeting:>10}') # 10칸 중 오른쪽 정렬
print(f'{3.141592:.4f}') # 소수점 4자리까지 표시

my_str = 'hello'

#인덱싱
print(my_str[0]) # h

#슬라이싱
print(my_str[2:4]) # ll
print(my_str[:3]) # hel
print(my_str[2:]) # llo
print(my_str[0:5:2]) # [start:end:step]
print(my_str[::-1]) # 슬라이싱으로 문자열 뒤집기

#길이
print(len(my_str)) # 5

# 리스트
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'python', ['hello', 'world', '!']]

print(my_list_3[-1][1][0])

my_list = [1, 2, 3]
my_list[0] = -1 # 리스트는 가변형 데이터 
print(my_list)

# tuple(변경 불가능한 리스트, 파이썬 내부 동작을 위한 타입)
my_tuple_1 = ()
my_tuple_2 = (1, ) # 튜플의 요소가 1개인 경우 반드시 ,필요
my_tuple_3 = (1, 'a', 3, 'b', 5)

# my_tuple_3[1] = 'z' # 변경 불가, 타입에러 발생

# range(연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형)
my_range_1 = range(5)
my_range_2 = range(10, -1, -1)
# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_2))

## Non-sequence type
# dict(key-value쌍, 순서x, 중복x)
my_dict_1 = {} # 빈 딕셔너리 생성
my_dict_2 = {'number': 12, 'list': [1, 2, 3]}

# 딕서너리의 값에 접근하기 위해서는 키값을 알아야함
print(my_dict_2['number']) # 12
my_dict_2['number'] = 100 # 가변형 자료형, 키값은 변경 불가

# set(순서x, 중복x, 집합 연산 수행 가능)
my_set_1 = set() # 빈 세트 생성하기
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

#합집합
print(my_set_2 | my_set_3) # {1, 2, 3}
#차집합
print(my_set_2 - my_set_3) # {2, 3}
#교집합
print(my_set_2 & my_set_3) # {1}

#불변과 가변
my_string = 'hello'
# my_string[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)
# 리스트는 요소마다 각자의 메모리주소를 가지기 때문에 변경이 가능함
# 객체의 참조만을 모아놓은 컬렉션이라고 할 수 있음
print(id(my_list[0]), id(my_list[1]))

# 가변 데이터 사용시 주의할 점 (슬라이싱을 이용해 필요한 부분만 새로운 리스트로 만들어 사용함: 얕은 복사)
list_1 = [1, 2, 3]
list_2 = list_1 # 얕은 복사
from copy import deepcopy
list_3 = deepcopy(list_1)
#얕은 복사로 인한 오류 
list_1[0] = 100 
print(list_1) #[100, 2, 3]
print(list_2) #[100, 2, 3]
print(list_3) #[1, 2, 3]


