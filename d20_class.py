'''
반복문 제대로 사용하기
'''

# # packing : 여러 value를 하나의 sequence로 묶는 작업
# packed_values = 1, 2, 3, 4, 5
# print(packed_values)

# numbers = [1, 2, 3, 4, 5]
# a, *b, c = numbers # *를 패킹 연산자로 활용
# print(a, b, c)

# print('hi', 'hello', 'goodbye', 'tschuess', sep='-') # end='\n'이 기본값

# unpacking 
# *
# names = ['a', 'b', 'c']
# print(*names)

# # ** : 딕셔너리 언패킹
# def my_function(x, y, z):
#     print(x, y, z)

# my_dict = {'x': 1, 'y':2, 'z':5}
# my_function(**my_dict)


# library : 모듈과 패키지의 집합
# module 가져와서 활용하기
# import math / from math import pi, sqrt

# # 사용자 정의 모듈
# from my_math import *
# result = cal_add(10, 15)
# print(result)

# # package : 묘듈을 디렉토리 별로 모아놓은 것 
# from my_package.math import my_math
# from my_package.statistics import tools
# print(my_math.cal_add(1, 2))
# print(tools.mod(3, 2))

# ### 외부 패키지 사용하기 ###
# # pip install requests
# import requests

# url = 'https://random-data-api.com/api/v2/users'
# response = requests.get(url).json() # API 리퀘스트 결과 받아와서 json으로 변환한 뒤 할당하기
# print(response['address']['country'], response['password'], response['first_name'])
# print(response.get('address').get('country'))
# print(type(response))

'''
4일차 강의 내용
'''

# 조건문
# 조건식에는 비교 연산, 논리 연산, 멤버 연산 등이 들어간다.

# dust = int(input())

# if dust > 150:
#     if dust > 400:
#         print('외출을 다시 생각해보세요!')
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 50:
#     print('보통')
# else:
#     print('좋음')

# 예제 1 - 정수를 입력받아 짝수이면 'even', 홀수이면 'odd'출력
# num = int(input())

# if num % 2 == 1:
#     print('odd')
# else:
#     print('even')

# 예제 2 - 윤년 판독기

# year = int(input())

# if (year % 4 == 0) and (year % 100 != 0):
#     print('leap year')
# elif year % 400 == 0:
#     print('leap year')
# else:
#     print('common year')

# 반복문
# 예제 1 - 구구단 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {(i * j):0>2}')
#     print()

# 예제 2 - 직각 이등변 삼각형 오른쪽

# for i in range(5):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
        
# for i in range(5):
#     for h in range(4, -1, -1):
#         print(' ' * h, end='')
#     print()
#     for j in range(i + 1):
#         print('*', end='')

# 예제 3 - 직각 이등변 삼각형

# num = int(input())
# for i in range(1, num + 1):
#     for _ in range(num - i): # 띄어쓰기 횟수만큼 반복
#         print(' ', end='') #자동 줄바꿈 방지
#     print('*' * (2 * i - 1), end='')
#     for j in range(num - i):
#         print(' ', end='')
#     print()         

# 예제 4 - 직각 이등변 삼각형 왼쪽
num = int(input())
for i in range(1, num + 1):
    for _ in range(num - i): # 띄어쓰기 횟수만큼 반복
        print(' ', end='') #자동 줄바꿈 방지
    print('*' * i, end='')
    print()

# while문(반복 종료 조건을 while문 내부 코드 블럭에 반드시 명시)
'''
초기식
while 조건식:
    code...
    증감식
'''
# 예제 1 - continue이용하여 홀수만 출력하기

# i = 0
# while i < 10:
#     if i % 2 == 1:
#         print(i)
#         i += 1
#     else:
#         i += 1
#         continue
    

# 예제 2 - break를 이용하여 'Shall we close? (y/n)'문구에 y를 입력해야 반복문이 끝나고 the end를 출력

# while True:
#     ans = input('Shall we close? (y/n)')
#     if ans == 'y':
#         print('the end')
#         break
#     else:
#         continue


# 예제 3 - 정수를 입력받아 자릿수를 출력하기

# n = int(input('정수를 입력하세요: '))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)

# # list comprehension
# import math
# numbers = [1, 4, 9, 16, 25]
# sqrt_numbers = []

# # way 1
# for number in numbers:
#     sqrt_numbers.append(int(math.sqrt(number)))
# print(sqrt_numbers)
# # way 2
# new_list = [int(math.sqrt(number)) for number in numbers]
# print(new_list)
# # way 3
# new_list_2 = list(map(lambda x: int(math.sqrt(x)), numbers))
# print(new_list_2)

# new_list_3 = [int(math.sqrt(number)) for number in numbers if number % 2 == 0]
# print(new_list_3)

# pass 예시(코드 미작성으로 인한 에러 방지를 위해 문법상 pass사용)
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('todos/', views.todo_list) # todo_list라는 함수를 만들어 놓긴 했으나 아직 코드를 짜지 않은 경우 views.py의 함수의 코드블록에 pass사용
# ]

# enumerate
