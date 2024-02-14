# #1
# me = {"name" : "Eliza", "lastname" : "Abdillabekova" , "age" : 16 , "favorite color" : "black" }
# print(me)

# #2
# me["hobby"] = "listen to music"
# print(me)

# #3
# print(me["age"])

# #4
# me["favorite color"] = "dark blue"
# print(me)

# #5
# me.pop("name")
# print(me)

#1
# while True:
#     users = input("Введите число: ")
#     print(set(users))

#2
# users = {"Eliza","Aslan","Alina"}
# users.union("Ayzirek","Emil","Nuriza")
# print(users)

# def num_set(set1, set2):
#     num2_set=set1.union(set2) 
#     return num2_set

# set_u = {1,2,3,4}
# set_i = {3,4,5,6,}

# l_set = num_set(set_u,set_i)
# print(l_set)

#3
# users = {"Eliza","Aslan","Alina"}
# users.intersection("Ayzirek","Emil","Nuriza")
# print(users)

# def intersection_sets(set1, set2):
#     result_set = set1.intersection(set2)
#     return result_set

# set_u = {1,2,3,4}
# set_i = {3,4,5,6,}

# intersection_set = intersection_sets(set_u,set_i)
# print("Пересеение множеств:", intersection_set)

#4
# def dublicates(a_list):
#     unique = set(a_list)
#     result_list = list(unique)
#     return result_list

# original_list = [1,2,3,4,4,2,1,1,5]
#####i = set(original_list)
#####print(i)
# result_list = dublicates(original_list)
# print("Список без повторяющихся элементов: ", result_list)

#5
# def is_subset(set1,set2):
#     return all(element in set2 for element in set1)
# set_a = {1,2,3}
# set_b = {1,2,3,4,5,6}
# result = is_subset(set_a, set_b)

# if result:
#     print("set_a является подмножеством set_b.")
# else:
#     print("set_a не явяляется подмножеством set_b.")

#1
# original_set = frozenset([1,2,3,4,5])
# try:
#     original_set.add(6)
# except AttributeError as e:
#     print(f"Ошибка: {e}")

#2
# def compare_frozensets(set1,set2):
#     if set1 == set:
#         return "Множества равны"
#     elif set1.issubset(set2):
#         return "Первое подмножество является подмножестовм второго"
#     elif set2.issubset(set1):
#         return "Второе подмножество является подмножеством первого"
#     else:
#         return "Множества не пересекаются"
# frozenset1 = frozenset([1,2,3,4,5])
# frozenset2 = frozenset([3,4,5,6,7])
# result = compare_frozensets(frozenset1,frozenset2)
# print(result)
    
#3
# frozen_set = frozenset([1,2,3,4,5])
# list_from_frozenset = list(frozen_set)
# print(frozen_set)
# print(list_from_frozenset)
 
# #4
# frozen_set1 = frozenset([1,2,3])
# frozen_set2 = frozenset([3,4,5])

#5
# new_frozen_set = frozen_set1.union(frozen_set2)
# print("Первый frozenset:" , frozen_set1)
# print("Второй frozenset:" , frozen_set2)
# print("Новый frozenset (объединение):" , new_frozen_set)
# numbers = [1,2,3,4,5]
# doubled_numbers = [number * 2 for number in numbers]
# print(doubled_numbers)

#доп дз
# strings = ["apple","banana","cherry","date"]
# uppercased_strings = [string.upper() for string in strings]
# print(uppercased_strings)

# words = ["lala","kkak","sisi"]
# character_lists = [list (word) for word in words]
# print(character_lists)

# numbers = [1,27,335,4,25] 
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# strings = ["hello","world","python"]
# modified_stings = [string.upper() +"!" for string in strings]
# print(modified_stings)

