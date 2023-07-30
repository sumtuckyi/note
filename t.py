# a = '반짝 반짝 작은 별 아름답게 비치네'
# b = '동쪽 하늘에서도 서쪽 하늘에서도'
# c = '반짝 반짝 작은 별 아름답게 비치네'
# print(a, b, c, sep='\n')

# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공의 열쇠', '내면의 변화', '목표의 달성']
# ]

# backup_catalog = catalog[:] #얕은 복사

# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''
# backup_catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']

# print('catalog와 backup_catalog를 비교한 결과')
# # 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오. 
# print(catalog is backup_catalog)

# print('backup_catalog : ')
# print(backup_catalog)
# print()

# print('catalog : ')
# print(catalog)

# def sort_tuple(my_tuple):
#     new_tuple = ()
#     for i in range(1, 6):
#         if i in my_tuple:
#             new_tuple += (i, )
#         else:
#             new_tuple += (i, )
#     return list(new_tuple)

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# 아래 함수를 수정하시오.
# def sort_tuple(my_tuple):
#     new_tuple = ()
#     for i in my_tuple:
#         if i in range(1, 5 +1):
#             new_tuple += (i, )
#     for i in range(1, 5 +1):
#         if i not in my_tuple:
#             new_tuple += (i, )    
#     return tuple(sorted(new_tuple))

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# def even_elements(any_list):
#     n = 0
#     sub_list = [0]
#     result = []
#     for _ in range(len(any_list) + 1):
#         if any_list[0] % 2 == 1:
#             any_list.pop(0)
#             any_list.extend(sub_list)
#         elif any_list[0] % 2 == 0:
#             if any_list[0] == 0:
#                 break
#             result.append(any_list[0])
#             any_list.pop(0)
#             any_list.extend(sub_list)
#     return result
    
    
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)


# # 아래 함수를 수정하시오.
# def count_character(str1, str2):
#     return str1.count(str2)
    

# result = count_character("Hello, World!", "o")
# print(result) # 2


# def find_min_max(my_list):
#     min_result, max_result = min(my_list), max(my_list)
#     print(type((min_result, max_result)))
#     return (min_result, max_result)
    

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)

# def union_sets(set1, set2):
#     return set1 | set2

# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# def get_value_from_dict(dictionary, key):
#     return dictionary[key]

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result) # Alice


# def remove_duplicates_to_set(list):
#     return set(list)

		
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 1
def add_item_to_dict(dictionary, key, value):
    dictionary.setdefault(key, value)
    return dictionary

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

# 2
def add_item_to_dict(dictionary, key, value):
    new_dict = {key: value}
    dictionary.update(new_dict)
    return dictionary

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)