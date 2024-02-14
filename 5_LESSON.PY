student = {"name": "Eliza" , "age" : 12 , "from" : "KR" }
# school = {"class" : 5}
# print(student["name"])
# print(student["age"])
# student["hobby"] = "Играть"  #для добавления нового объекта
# print(student)
# student["from"] = "KZ"    #для изменения объекта
# print(student)
# student.pop("name") #для удаления объекта
# del 
# print(student)
# student.update(school)  #для объединения двух словарей
# print(student)
# print(student.values()) #только инфу
# print(student.keys()) #Только ключи
print(student.items()) 


#создаются с помощью фигурных скобок
#Не имеет структуры и определенного порядка (индекс,срезов)
#Не имеет дубликатов 
# set изменяемый
#frozenset неизменяемый


users = {"Nurbolot","Geeks","Islambek","Beksultan"}
print(users)
users.add("Anton")
print(users)
print(users[1]) #Не работает индексы

# users = frozenset(["Nurbolot","Vlad","Georgiy","Ilya"])
# users.add("Kutkubak")
# print(users)
# users.remove("Geeks")
# print(users)

# while True: 
try: 
       num1 = 3131
       num2 = "2393"
       print(num1+num2)
except TypeError:
       print("число нельзя сложить на буквы")

try: 
    number1 = 100
    number2 = "0"
    print(number1/number2)
except TypeError:
    print("На ноль делить нельзя")

try:
    hd = [1,2,3,4,5]
    hd.remove(10)
    print(hd)
except :
     print("Такого объекта нет")


try:
     numbers = [11,33,28,92,19]
     numbers.remove(12)
     print(numbers)
except:
     print("Такого числа нет")

try:
     cars = ["Toyota","Lexus","BMW"]
     cars.remove("Tesla")
     print(cars)
except:
     print("Такой машины нет в списке")


try:
     music = ["kiss","love","tornado"]
     music.remove("Lala")
     print(music)
except:
     print("Вы не скачивали эту музыку")


try: 
    food = ["Burger","Cola","Free"]
    food.remove("Chicken")
    print(food)
except:
     print("Эта еда здесь не продается")


try:
     item = ["Biology","Histiry","English"]
     item.remove("Math")
     print(item)
except:
     print("Этого предмета нет в расписании")

