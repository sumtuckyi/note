# data structure
# 시퀀스 데이터 구조와 그 메서드

# 각 데이터 구조의 메서드를 호출하여 활용하기(메서드는 클래스별로 정의됨)
# 메서드 : 객체에 속한 함수 

# class : type을 표현하는 방법

# print(help(list))
'''
class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
'''

# 메서드 호출하기 : 데이터 타입 객체.메서드()

# Sequence Type에서 메서드 활용하기
# 1. 문자열 
# 문자열 조회/탐색 및 검증 메서드
### 공식문서상에서 해당 메서드가 파괴적(원본 데이터를 변형)인지 비파괴적(변형한 복사본을 반환)인지 구분할 것
# s = 'hello'
# print(s.find('s')) # 해당 문자열의 가장 앞쪽 위치 인덱스를 반환, 없으면 -1을 반환
# print(s.index('o')) # 4 , find와 달리 없으면  error발생
# print(s.isalpha()) 
# print(s.islower()) # True, 문자열 전부가 소문자여야 True 
# print(s.isupper())

# 문자열 조작 메서드 : 새로운 문자열을 반환
# print(s.replace('l', 'k', 1)) # 'l'을 'k'로 대체하는데 단 처음 하나의 문자열만
# print('     Hello, world!    '.strip())
# print('hello, world!'.title())
# print('heLLO, wOrlD!'.swapcase())

## split과 join
# print('snow yuki'.split(' ')) # 인자를 기준으로 iterable을 자르는 메서드
# print(' '.join('hello')) # 인자를 객체인 문자열을 구분자로 이용하여 하나의 문자열로 연결하는 메서드

# 기타 메서드
#''.isdecimal() -> ''.isdigit() -> ''.isnumeric() 순으로 갈수록 넓은 범위의 문자를 숫자로 판별함 

# 2. 리스트
# 값 추가 및 삭제 메서드
new_list = [1, 2]
# 요소 추가하기
## new_list.append(3) # 단일 요소로서 정수를 추가(가장 마지막에 추가됨)
# new_list.append([4, 5]) # 단일 요소로서 리스트를 추가
## new_list.extend([4, 5]) # ITERABLE의 개체를 순차적으로 모두 추가 / 결합 연산자 기능
# print(new_list.append(10)) # append메서드는 파괴적 메서드로 원본을 변형함
# print(new_list) 
# new_list.insert(0, -1) # 지정한 위치에 요소를 추가하기
# print(new_list) 
# 요소 삭제하기
# new_list.remove(4) # 리스트에 첫 번째로 일치하는 항목을 삭제 / 항목이 존재하지 않을 경우 에러 발생
# print(new_list) 
## deleted_value = new_list.pop(0) ## 지정한 인덱스의 값(없다면 가장 마지막 요소)을 삭제하고 그 값을 반환함(삭제한 값을 확인할 수 있어 유용함)
# print(deleted_value)
# new_list.clear()
# print(new_list)

# 리스트 탐색 및 정렬 메서드 : 원본 리스트를 변형!!
# new_list = [0, 1, 2, 3, 4, 5, 0, 1, 2]
# index_of_value = new_list.index(2)
# print(index_of_value) # 2
# print(new_list.count(0)) # 2
## 메서드인 sort()와 내장함수인 sorted()
# new_list.sort() # 원본 리스트를 오름차순으로 정렬
# sorted_list = sorted(new_list) # 내장함수인 sorted(list)는 변형된 리스트(복사본)를 반환(원본을 변형하지 않음)
# print(new_list, sorted_list)
# new_list.sort(reverse=True) # 원본 리스트를 내림차순으로 정렬, 기본 매개변수가 reverse = False였음을 알 수 있음
# print(new_list)
# new_list2 = [2, 1, 9, 7, 4]
## new_list2.reverse() # 정렬이 아니라 순서만 뒤집는 것
# print(new_list2)

# 예시 - 리스트 복사하여 사용하기 
numbers = [1, 2, 3]
# 1.할당
list1 = numbers # list1과 numbers는 같은 메모리 주소를 바인딩함
# 2.슬라이싱
list2 = numbers[:] # ITERABLE을 슬라이싱하면 복사본을 반환한다(즉, 원본과 다른 메모리 주소를 가짐)

numbers[0] = 100
print(list1) # [100, 2, 3]
print(list2) # [1, 2, 3]

# 3.deepcopy()



