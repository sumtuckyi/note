'''
sequence type
'''

# decimal = 16
# #1. 2진수로 출력
# print(bin(decimal)[2:])

# #2. 8진수
# print(oct(decimal)[2:])

# #3. 16진수
# print(hex(decimal)[2:])

# f-string 사용해서 부동소수점의 정확도 제어하기
# a = 3.2 - 3.1
# b = 1.2 - 1.1

# print(f'{a:.1f}, {b:.1f}')

# 거듭제곱의 지수 표현, 산술연산자 표현
# print(314e-2, 314 * 10 ** -2)

# f-string 사용해서 출력값 정렬하기
# greeting = 'hi'
# print(f'{greeting:>10}') # 10칸 중에 오른쪽 정렬
# print(f'{greeting:^10}')
# print(f'{greeting:<10}')

### Sequence type ###
# 문자열 parsing하기
greeting = 'hello world'

#1. indexing
print(greeting[6])

#2. slicing
print(greeting[:5])
print(greeting[6:])
# step이 양수이면 end-1까지, step이 음수이면 end+1까지

#3. reverse
print(greeting[::-1])

for i in range(len(greeting) - 1, -1, -1):
    print(greeting[i], end='')

print()

#4. length
print(len(greeting))

#5. for문 활용(2가지 방식)
for i in range(len(greeting)):
    print(greeting[i], end='')

print()

for i in greeting:
    print(i, end='')
