# 7월 19일

# function
# 함수 정의
# def greet(name): # 여기서 매개변수는 name
#     message = 'Hello, ' + name
#     return message # return키워드 이후에 반환할 값을 명시 , return문은 함수의 실행을 종료함

# # 함수 호출
# result = greet('Alice') # 함수 호출시 전달되는 값인 인자가 여기서는 'Alice'
# print(result)

# #기본 인자(매개변수에 기본값 할당)
# def greet2(name, age = 30):
#     print(f'안녕하세요, {name}! {age}살이군요.')

# greet2('Bob')

# #위치 인자, 키워드 인자(함수 호출시 특정 매개변수에 값을 할당)
# def greet3(name, age):
#     print(f'안녕하세요, {name}! {age}살이군요.')

# greet3(25, "Alice") # 위치인자 예시. 안녕하세요, 25! Alice살이군요.
# greet3(age = 25, name= 'Alice')

# # 정해지지 않은 개수의 인자(arbitraty argument lists)를 처리하는 함수
# # 예시 print('a', 'b', 'c')

# def cal_sum(*args):
#     print(args) # (1, 2, 3) tuple
#     total = sum(args)
#     print(f'합계: {total}')

# cal_sum(1, 2, 3)

# def print_info(**keyargs):
#     print(keyargs) # {'name': 'Alice', 'age': 20} dict

# print_info(name = 'Alice', age = 20)

# SCOPE
# local scope
# def func():               # local scope
#     num = 20              # local scope
#     print('local', num)   # local scope

# func()
# print('global', num) # num is not defined 오류 발생

#LEGB rule - local scope -> enclosed scope -> global scope -> built-in scope
# 내장 함수나 키워드의 이름을 변수명으로 쓰면 이름검색규칙에 의해 원래 내장함수나 식별자를 제 기능대로 사용하지 못하게 된다. 
# LEGB rule 예시
# a = 1
# b = 2

# def enclosed():
#     a = 10
#     c = 3

#     def local(c):
#         print(a, b, c)

#     local(500)
#     print(a, b, c)

# enclosed()
# print(a, b)    

# 함수 내에서 전역변수를 참조만 하는 것이 아니라 수정까지 하고 싶은 경우(전역 변수를 함수 내에서 수정하는 경우 그 변수를 이미 사용하던 코드에 영향을 미치게 되므로 권장하지 않음)
# num = 0

# def increment():
#     global num # num을 전역변수로 선언
#     num += 1 # 전역 변수의 값을 수정

# print(num)
# increment()
# print(num)

# 재귀 함수 예시(스택 자료구조 사용)
# def factorial(n):
#     if n == 0: # 종료 조건
#         return 1
#     return n * factorial(n - 1) # 재귀 호출

# result = factorial(5)
# print(result)

# 알아두면 유용한 함수 -1 : map()
numbers = [1, 2, 3]
result = map(str, numbers) # map object를 반환
# map() + lambda함수 
result2 = map(lambda x: x * 2, numbers) # 필요에 따라 내가 만든 함수를 첫 번째 인자로 전달할 수 있어 매우 유용
print(list(result))
print(list(result2))

# 알고리즘 문제 입력값 저장 방식 예시
# import sys

# sys.stdin = open('input.txt')
# t = int(input())
# k, n, m = map(int, input().split()) # map unpacking

# 알아두면 유용한 함수 -2 : zip(*iterables)
# example_1
names = ['a', 'b', 'c']
cities = ['London', 'New York', 'Paris']

for name, city in zip(names, cities):
    print(f'{name} lives in {city}')

# example_1
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

