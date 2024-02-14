# #1
# i = 0
# for i in range(5):
#     print(0)

# #2
# numbers = []
# for num in range(1,101):
#     numbers.append(num)
# print(numbers)    

# #3 
#for numbers in range(2,497,2):
#     print(numbers)
# #4
# numbers = []
# for num in range(1,1001):
#     numbers.append(num)
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# #5
# numbers = []
# for num in range(100):
#     print(0)

# #6
# numbers = input("Введите первую переменную: ")
# numbers2 = input("Введите вторую переменную: ")
# numbers, numbers2 = numbers2, numbers
# print(numbers,numbers2)

# #1
my_tuple = ("Get out","Solstice","Pearl")
print(type(my_tuple))

# #2
reset_my = list(my_tuple)
print(type(reset_my))
reset_my.pop(1)
my_tuple=tuple(reset_my)
print(my_tuple)

# #3
# a_tuple = ("котики","собачки","панда","попугай")
# b_tuple = ("черный","белый","зеленый","синий")
# print(a_tuple+b_tuple)

# #4
# num_tuple = (1,2,3,4,5)
# print(len(num_tuple))

# #5 
# p_tuple = (1108909314)
# n_tuple = (1102373314)
# print(p_tuple==n_tuple)


# #допдз
# name = input("Введите имя: ")
# while True:
#     age = int(input("Введите возраст: "))
#     if age <18:
#      print("Вам нет 18")
#     else:
#      print("Добро пожаловать")

#допдз2
# l_tuple = ("Geeks","Eliza","helpme")
# print(type(l_tuple))
# reset_l = list(l_tuple)
# print(type(reset_l))
# reset_l.append("Geeks2")
# l_tuple = tuple(reset_l)
# print(l_tuple)