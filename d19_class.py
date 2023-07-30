'''
2일차 내용인 데이터 타입 복습
-가변성 유의 
문자열:'', 문자열 파싱 문제
리스트:[], 방향배열 문제, BFS, DFS 문제 2차원 배열을 주로 사용함
튜플: (), 방향배열 문제
딕셔너리: {key:value}, 키는 불변 자료형이어야 함. Key-value쌍으로 이루어짐. 키를 통해 value에 접근
세트: {}, set()로 선언, 중복을 허용x, 집합 연산 시 사용 
'''

# 2차원 배열의 가독성을 높이는 코드 작성법
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# # 인덱싱으로 3을 출력
# print(arr[0][2])
# # 7을 출력
# print(arr[2][0])

# # 2차원 리스트 입력받기
# rows = int(input("행의 개수를 입력하세요."))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for row in matrix:
#     print(row)

# Tuple 사용예시
# def move_around(position):
#     x, y = position 
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 현재 위치를 중심으로 상하좌우
#     directions2 = [(1, 1), (-1, 1), (1, -1), (-1, -1)] # 현재 위치를 중심으로 대각선방향으로 시계방향

# range는 주로 반복문과 사용
# print(list(range(5)))
# print(list(range(2, 5))) # end는 포함하지 않음
# print(list(range(1, 10, 2))) # 홀수만 출력
# print(list(range(10, 0, -1))) # 역순으로 출력(step을 음수로)

# # dict
# # 2차원 딕셔너리
# my_dict = {
#     'a1': {'b1': 1,'b2': 2, 'b3': 3},
#     'a2': {'b1': 4,'b2': 5, 'b3': 6},
#     'a3': {'b1': 7,'b2': 8, 'b3': 9}
# }

# # value 5를 출력하기
# # way1 
# print(my_dict['a2']['b2']) # 딕셔너리의 value에는 key를 통해 접근 가능
# # way2 - 내장함수 사용하기
# print(my_dict.get('a2').get('b2'))

# # set
# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4, 5, 6, 7, 8, 9}

# #합집합
# print(set_1 | set_2)

# #차집합
# print(set_1 - set_2)

# #교집합
# print(set_1 & set_2)

# set 사용 예시
# import random

# set_1 = set()

# while len(set_1) < 6:
#     number = random.randint(1, 45)
#     set_1.add(number)

# lotto_list = list(set_1)
# lotto_list.sort() # sort는 원래 리스트의 순서를 바꿀 뿐 새로운 리스트를 반환하지는 않는다. 
# print(lotto_list)

'''
정수 -> False : 0
실수 -> False : 0.0
문자열 -> 
'''

# 명시적 형변환
# str -> int
# int -> str // 문자열의 불변성과 시퀀스를 이용하기 위함
# float -> int // 소수점 이하 버림
# int(float('3.5'))

# 연산자
numbers = [1, 2, 3, 4, 5]

# 복합연산자
# total = 0

# for num in numbers:
#     total += num

# print(total)

# 식별 연산자 is,  is not : 변수가 바인딩하는 객체의 메모리 주소가 동일한지 비교

# 논리 연산자 and, or, not
# 한 줄의 코드 내에서 왼쪽에서 오른쪽 방향으로 연산 수행
# vowels = 'aeiou'

# print(('a' and 'b') in vowels) # 'b' in vowels
# print(('a' or 'b') in vowels) # 'a' in vowels
# print(('b' and 'a') in vowels) # 'a' in vowels

# print(3 and 5 and 7) # 7
# print(3 and 0) # 0
# print(3 and 0 and 5) # 0
# print(0 and 3) # 0
# print(0 and 0) # 0

# print(5 or 3) # 5
# print(3 or 0) # 3
# print(0 or 3) # 3
# print(0 or 0) # 0 

# 멤버십 연산자
# word = 'hello'
# numbers = [1, 2, 3, 4, 5]

# print(4 not in numbers)

'''
3일차 내용 진도 마저 나가기(함수가 핵심)
'''

# 함수
# 프로그램의 유지, 보수, 코드의 가독성을 위해 함수를 사용한다. 
# 함수 선언(매개변수와 반환값은 각각 있을 수도 있고 없을 수도 있음)
'''
def 함수명(매개변수):
    ...     #함수 바디
    return 반환값
'''
# 함수 호출
'''
함수명(인자)
'''

# # 동일한 기능을 수행하는 함수를 어떻게 다양하게 작성할 수 있을까
# # 기본 함수
# def get_sum(num1, num2):
#     return num1 + num2

# # 매개변수가 없는 형태
# def get_sum1():
#     num1 = 1
#     num2 = 2
#     return num1 + num2

# # return이 없는 형태
# def get_sum_2(num1, num2):
#     print(num1 + num2)

# print(get_sum(1, 2))
# print(get_sum1())
# get_sum_2(1, 2)

# # 위치 인자(함수 호출 시 인자의 위치에 따라 매개변수와 매핑됨)
# def greet(name, age):
#     print(f'안녕하세요. {name}! {age}살이시군요~')

# greet('예준', 26)
# greet(30, 'Anna')

# # default 인자(정확히 말하면 함수 선언시 인자값을 고정하는 것, 매개변수의 뒤에서부터)
# def greet2(name, age = 20):
#      print(f'안녕하세요. {name}! {age}살이시군요~')

# greet2('yejun')

# # keyword 인자(인자 전달시 순서가 바뀌어도 적당한 매개변수와 매핑된다.)
# # 키워드 인자와 위치 인자는 함께 사용할 수 없다. 
# greet(age = 19, name = 'yj')

# # 가변 인자 목록
# def calculate_sum(*args):
#      print(args) # 다수의 인자를 튜플로 처리한다. 
#      total = sum(args)
#      print(f'총합은 {total}입니다.')
    
# calculate_sum(3, 5, 7, 8, 44)

# # 가변 키워드 인자
# def print_info(**kwargs):
#      print(kwargs) # 키워드와 값을 딕셔너리로 처리한다.

# print_info(name = 'yejun', height = 180, age = 20)

# # scope
# '''
# local scope : 함수 안
# enclosed scope : 현 스코프를 포함하는 가장 인접한 스코프
# global scope: 현재 프로그램 내부
# built-in scope: 내장함수나 예약어
# '''

## 예시 1
# z = 0
# def outer(): # x를 local scope에서 찾을 수 있음
#     x = 1
#     def inner(): 
#         y = 2
#         result = x + y # x를 찾으려면 enclosed scope를 탐색해야함
#         print(result)
#     inner()

# outer()

## 예시 2
# a, b, c = 1, 2, 3

# def enclosed():
#     global a, b, c
#     a, b, c = 4, 5, 6
#     def local(c):
#         print(a, b, c) # 4 5 500
    
#     local(500)
#     print(a, b, c) # 4 5 6

# enclosed()
# print(a, b, c) # 1 2 3 global선언시 4 5 6

# # 재귀함수
# # 가장 간단한 형태
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
    
# print(factorial(10))

# map(), zip()
# lambda 함수 : 표현식의 내용이 반환되므로 return문이 필요없고, 재사용하지 않기 때문에 함수명이 필요없다. 

# numbers = [1, 2, 3, 4, 5]
# numbers_list = list(map(lambda x : x ** 2, numbers))
# print(numbers_list)
