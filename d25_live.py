# 비시퀀스 데이터 구조

# 1. 세트 : 고유한 항목들의 정렬되지 않은 컬렉션(세트의 요소는 해시함수를 통해 해시주소를 가지게 되며, 해시테이블에 저장된 순서대로 출력)
# 관련 메서드
ss = {1, 2, 3}

ss.add(4)
ss.add(4)
#print(ss) # {1, 2, 3, 4} 
ss.clear()
#print(ss) # set() : 빈 세트

ss = {1, 2, 3}

ss.remove(1) # 항목이 없을 경우 키에러 발생
#print(ss) # {2, 3}
ss.discard(4) # 없는 항목을 삭제하려고 하여도 에러가 발생하지 않음
# print(ss.discard(4)) # None
# print(ss) # {2, 3}
# print(ss.pop()) # 2, 임의의 요소를 삭제하고 그 요소를 출력함(해시 테이블 상의 특정 주소에 있는 값을 가져옴(테이블에 나타난 주소의 순서대로 가져옴), 해시함수로 인해 원래는 테이블 상에서의 주소에 바인딩된 값이 바뀌는데 키가 정수와 같이 불변 자료형인 경우에는 해시함수를 통해 나온 주소가 변하지 않는다.)
# print(ss) # {3}


ss.update({'1':'a'}) # 키값(str)만 요소로 추가됨
#print(ss) # {3, '1'}
ss.update([1, 2, 3]) # iterable의 요소를 추가하며 그 자체는 리스트로서 가변적인 데이터(not hashable)이기 때문에 세트의 요소로 추가될 수 없다. 
#print(ss) # {1, '1', 3, 2}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
# set1 - set2
set1.difference(set2)
# set1 & set2
set1.intersection(set2)
# set1 <= set2
set1.issubset(set2)
# set1 >= set2
set1.issuperset(set2)
# set1 | set2
set1.union(set2)

# 2. 딕셔너리 : 고유한 항목들의 정렬되지 않은 컬렉션(키값이 중복될 수 없음)
person = {
    'name': 'Alice',
    'age': 20,
    'country': 'USA'
}

value_from_key = person.get('name')
# print(value_from_key) # Alice
# print(person['name']) # Alice
# 찾고자 하는 키가 없을 때
print(person.get('hobby')) # None / dict.get(key[, default])
# print(person['hobby']) # KeyError

print(person.keys()) # dict_keys(['name', 'age', 'country'])
for key in person.keys():
    print(key)

print(person.values())
for value in person.values():
    print(value)

print(person.items())
for key, value in person.items():
    print(f'{key}: {value}')

print(person.pop('country')) # USA
print(person.pop('hobby', '해당 키는 존재하지 않습니다.')) # 해당 키는 존재하지 않습니다.
# 키와 연결된 값을 반환, 키가 없다면 인자로 받은 키와 값을 추가
print(person.setdefault('hobby', 'watching movie')) # watching movie / 해당 키가 없다면 전달받은 키와 값을 새로운 요소로 추가 가능(조건문으로 구현하던 과정 대체 가능)
print(person)
# 기존 키를 덮어쓰면서 딕셔너리를 갱신하는 메서드
other_person = {
    'name': 'Jane',
    'gender': 'Female'
}
person.update(other_person) # 딕셔너리 자체를 인자로 주거나
print(person)

person.update(age = 50) # 하나의 키-값 쌍만 인자로 줄 수도
print(person)

# 키를 이용한 딕셔너리 조회
# 예제 
blood_types = ['A', 'B', 'O', 'AB', 'A', 'A', 'O', 'AB', 'B']
# 1 : ['']
new_dict = {}
for blood_type in blood_types:
    if blood_type in new_dict:
        new_dict[blood_type] +=1
    else:
        new_dict[blood_type] = 1
print(new_dict)

# 2 : .get()
new_dict = {}
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1 # 키값이 없으면 default값만 반환
    # if blood_type in new_dict:
    #     new_dict[blood_type] +=1
    # else:
    #     new_dict[blood_type] = 1
print(new_dict)

# 3 : .setdefault()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0) # 키값이 없으면 해당 키-값 쌍을 딕셔너리에 추가함
    new_dict[blood_type] +=1
    # new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)

# 복사
## 변경 가능한 데이터 타입의 복사
# 변경 불가능한 데이터 타입의 복사

# 1. 할당
original_list = [1, 2, 3]
copy_list = original_list
print(original_list is copy_list) # True
print(original_list, copy_list)

# 2. 얕은 복사 - 2차원 리스트가 아닌 경우에는 문제 없음 
a = [1, 2, 3]
b = a[:]
c = a.copy()
b[1] = 200
print(a is b) # False
print(a, b, c) # [1, 2, 3] [1, 200, 3] [1, 2, 3]
## 2차원 리스트를 얕은 복사하는 경우 ##
A = [1, 2, [1, 2]]
B = A[:]
B[2][0] = 100
print(A, B) # [1, 2, [100, 2]] [1, 2, [100, 2]]

# 3. 깊은 복사
import copy 
aa = [1, 2, [1, 2]]
bb = copy.deepcopy(aa)
bb[2][0] = 100
print(aa, bb) # [1, 2, [1, 2]] [1, 2, [100, 2]]