# 문자열 메서드
'''
find() - r(Return method)
rfind() - r
index() - r
isalpha() - r
islower() - r
isupper() - r
replace(old, new[, count]) - r
strip() - r
capitalize() - r
title() - r
swapcase() - r
split() - r
'separator'.join(str) - r
isdecimal() - r
isdigit() - r 
isnumeric() - r
'''

# 리스트 메서드
'''
append() - v(Void method)
extend() - v
insert(index, value) - v
remove() - v
clear() - v
pop(index) - r
index(value[,start[, end]]) - r
count() - r
sort(reverse= False) - v
reverse() - v
copy() - r , 얕은 복사(서로 다른 메모리 주소를 바인딩함, 2차원 리스트가 아닌 경우에는 문제 없음)

'''
# 문자열 메서드 실습
s = "Practice makes perfect"

# 1
counts_e = s.count('e') # 4
# 2
index_of_character = s.find('i') # 5, 찾는 문자열이 없으면 -1을 반환/ 가장 앞에 있는 값의 인덱스를 반환
index_of_character2 = s.index('i') # 5, 찾는 문자열이 없으면 에러가 발생
# 3
list_of_string = s.split(' ') # ['Practice', 'makes', 'perfect']
# 4
replaced_string = "makes".replace('k', 'd').replace('s', '') # made
# 5
uppercase = s.upper() # PRACTICE MAKES PERFECT
lowercase = s.lower() # practice makes perfect
# 6
stripped = "   Practice makes perfect   ".strip() # Practice makes perfect
# 7 
joined = '.'.join(s) # P.r.a.c.t.i.c.e. .m.a.k.e.s. .p.e.r.f.e.c.t

print(counts_e, index_of_character, index_of_character2, list_of_string, sep='\n')
print(replaced_string, uppercase, lowercase, stripped, joined, sep='\n')

print(ord('A')) # 문자열의 아스키 코드값을 변환하는 함수 ord()
print(ord('a'))
print(chr(ord('A'))) # 아스키 코드값을 문자열로 변환하는 함수 chr()

# 리스트 메서드 실습 
l = ['b', 'a', 'n', 'a', 'n']

# Void methods : 주로 원본을 변경
# 1
l.append('a')
print(l)
# 2
l.sort() # 오름차순
print(l)

print(sorted(l)) # 내장함수 sorted는 원본을 변경하지 않고 오름차순으로 변환한 복사본을 반환

l.sort(reverse= True) # 내림차순
print(l)
print(sorted(l, reverse=True))
# 3
l.reverse() 
print(l)
# 4
a_removed = l.remove('a') # 처음 일치하는 하나의 값만 삭제함/ 항목이 존재하지 않을 경우에는 에러가 발생하므로 해당 문자열을 포함하는지 먼저 확인하고 메서드를 사용할 것
print(l)

# Return methods
# 5
deleted_value = l.pop() # 인자를 전달하지 않으면 뒤에서부터 삭제
print(deleted_value)
# 6
counts_n = l.count('n')
print(counts_n)