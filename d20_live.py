# 7월 20일

## 제어문(조건문, 반복문)
# 조건문(if, elif, else)
# 예시
# num = int(input('숫자를 입력하세요 : ')) 

# num이 홀수라면
# if num % 2 == 1:
#     # if num % 2:             # 0은 False로 평가되지만 나머지 정수는 True로 평가
#     print('홀수입니다.')
# # num이 홀수가 아니라면
# else:
#     print('짝수입니다.')

# 반복문(for, while)
# 'for' statement : 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복(종료조건이 필요x)
# iterable = [1, 2, 3]
# iterable2 = 'Hello' # 문자열도 반복 작업을 수행할 수 있음!!
# iterable3 = (1, 2, 3)
# iterable4 = {1, 2, 3} # 세트
# iterable5 = {'a': 1, 'b':2, 'c':3}
# iterable6 = range(10)
# for i in range(len(iterable)):
#     # print(variable, end='')
#     iterable[i] = iterable[i] * 2

# print(iterable)

# 중첩된 반복문
# 2차원 리스트를 중첩 반복문으로 다루는 연습

# 'while' statement : 주어진 조건식이 True인 동안 코드를 반복(즉, 조건식이 거짓이 될 때까지 반복)
# 종료조건을 정확하게 설정해주어야 코드가 제대로 동작함
# 예시
# num = int(input())

# while num <= 0:
#     if num < 0:
#         print('양의 음수 말고 양의 정수를 입력해주세요.')
#     else:
#         print('0말고 양의 정수를 입력해 주세요.')
#     num = int(input())
# print('잘했습니다.')    

# # 종료조건 만들기
# while num <= 0:
#     if num == -1000:
#         break
#     if num < 0:
#         print('양의 음수 말고 양의 정수를 입력해주세요.')
#     else:
#         print('0말고 양의 정수를 입력해 주세요.')
#     num = int(input())
# print('잘했습니다.') 

numbers = list(range(11))

# # continue 사용하기(코드의 가독성과 의도를 생각하여 사용)
# for num in numbers:
#     if num % 2 == 0: # num이 짝수이면 다음 반복으로 넘어가므로 아래의 print문이 수행되지 않음
#         continue
#     print(num)

# # break 사용하기
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         break
# print('짝수를 찾았습니다.')   

# list comprehension
# my_list = [[0 for i in range(10)] for j in range(10)]
# my_list2 = list([0 for i in range(10)] for j in range(10))

# print(my_list, my_list2, sep='\n')

# # 특정 범위의 리스트 만들기
# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list)

# # 2. list comprehension (편리할 수 있으나 가독성이 떨어지고 코드의 의도를 전달하기 어려움)
# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)
# squared_numbers = [i ** 2 for i in range(10)]
# print(squared_numbers)
# new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)] # elif는 사용 불가
# print(new_list_3)

# # list 생성방식 비교
# numbers = ['1', '2', '3']

# # 1. for loop
# new_nembers = []
# for i in numbers:
#     new_nembers.append(int(i))
# print(new_nembers)

# # 2. map()
# new_numbers_2 = list(map(int, numbers)) # 함수를 인자로 전달할 수 있다는 장점 때문에 써야하는 상황이 있음
# print(new_numbers_2)

# # 3. list comprehension
# new_numbers_3 = [int(i) for i in numbers]
# print(new_numbers_3)

# enumerate - 반복문에서 인덱스 값을 활용하고 싶을 때 range(len(arr))대신 사용
fruits = ['apple', 'banana', 'cherry']
print(list(enumerate(fruits))) # [(index, element)]
      
for index, fruit in enumerate(fruits): # enumerate는 튜플의 형태
    print(f'인덱스 {index}: {fruit}')

