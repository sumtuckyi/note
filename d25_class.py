# set method
'''
add() - v
update(iterable) - v
remove() - v, KeyError
discard() - r
clear() - v
pop() - r
difference() - r
intersection() - r
union() - r
issubset() - r
issuperset() - r
'''

# dictionary method
'''
get(k[, default]) - r
keys() - r
values() - r
items() - r
pop(k[, default]) - r
setdefault(k, value) - r(해당 키가 있다면 매치된 값을 반환)
update() - v
clear() - v
'''

# set
list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 7, 8, 9]
set1 = set(list_1)
set2 = set(list_2)

# 1
set1.add(4)
#print(set1) # {1, 2, 3, 4}
# 2
set1.update([5, 6, 7])
#print(set1) # {1, 2, 3, 4, 5, 6, 7}
# 3
set1.remove(7) # {1, 2, 3, 4, 5, 6}
#print(set1)
#print(set1.discard(7)) # None 
# 4
#print(set1.difference(set2)) # {1, 2, 3}
# 5
#print(set1.intersection(set2)) # {4, 5, 6}
# 6
#print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#print(list(map(hash, list_2)))

# dictionary
my_dict = {
    'plus': ['더하기', '장점'],
    'minus': ['빼기', '적자'],
    'multiply': ['곱하기', '다양하게'],
    'division': ['나누기', '분열']
}

# 1
# word = input()
# print(*my_dict.get(word))
# print(my_dict[word])
# print(my_dict.setdefault(word))

# 2
print(list(my_dict.keys()))

# 3
new_dict = {
    'square': ['제곱', '사각형']
}

my_dict.update(new_dict)
print(my_dict)

my_dict.setdefault('square', ['제곱', '사각형'])
print(my_dict)

my_dict['square'] = ['제곱', '사각형']
print(my_dict.items())

# 4
# word2 = input()
# my_dict.pop(word2)

# del my_dict[word2]
# print(my_dict)

# 예제 
blood_types = ['A', 'B', 'O', 'AB', 'A', 'A', 'O', 'AB', 'B']

from collections import Counter

print(Counter(blood_types))

# 불변 데이터는 원본이 변경되지 않는다.
# 할당
list1 = [1, 2, 3, 4]
list2 = list1
list2[0] = 5
print(list1 is list2) # True
print(list1, list2) # [5, 2, 3, 4] [5, 2, 3, 4]

# 얕은 복사 : 객체 안에 객체가 있는 경우 원본 데이터가 변경됨
list1 = [1, 2, [3, 4]]
list3 = list1[:]
list4 = list3.copy()
print(list3 is list1) # False 

list3[0] = 5
print(list1, list3) # [1, 2, [3, 4]] [5, 2, [3, 4]]
print(id(list1[0]), id(list3[0])) # 2181070285104 2181070285232
print(id(list1[2]), id(list3[2])) # 1798693272064 1798693272064
#print(id(list1[2][0]), id(list3[2][0])) # 2194443168112 2194443168112

# 깊은 복사
import copy
list5 = copy.deepcopy(list1)
print(id(list1[2]), id(list5[2])) # 2513286543936 2513286653120


