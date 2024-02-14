# def summ(num1,num2):
#     print(num1+num2)
# summ(27,22)

summ = lambda num1,num2:num1+num2
print(summ(2,3))

# summ = lambda num1,num2:num1%num2
# print(summ(82,17))

# users = input("Введите имя:")
# password = input("Введите пароль: {}")
# if password == {}:
#     print("Доступ разрешен")
# else:
#     print("пока")

# users = ["Mergul","Beksultan","Kutkubak","Anton"]
# result = list(map(lambda num: f"{num}-{len(num)} букв" , users))
# print(result)


# "Mergul"
# "Beksultsn"
# "Kutkubak"
# "Anton"


numbers =list(range(1,11)) 
result = list(map(lambda x: x + 5, numbers))  
print(result)


users = ["Mergul","Beksultan","Kutkubak","Anton"]
result = list(map(lambda num: num[0] , users))
print(result)

# users = ["Mergul","Beksultan","Kutkubak","Anton"]
# result = list(map(lambda num: num.upper(), users))
# print(result)

# num = int(input("Введите первое число:"))
# if num==+:
#      num2 = int(input("Введите второе число:"))
# num3 = (num,num2)
# result = list(map(lambda num: num*num2, num3 ))
# print(result)
# # result = list(map(lambda num: num*num2, num3 ))


users = ["Mergul","Beksultan","Kutkubak","Anton"]
result = list(map(lambda num: num.lower(), users))
print(result)

users = ["Mergul","Beksultan","Kutkubak","Anton"]
result = list(map(lambda num: num.title() , users))
print(result)


numbers = list(range(1,101))
result = list(map(lambda num: num % 2, numbers))
print(result)

