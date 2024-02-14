#задание 1
liza = "Я люблю эклеры.\n \"Эклеры \" моя любимая еда"
print(liza)

#задание 2
name = "Eliza "
lastname = "Abdillabekova "
age = "16 "
#Привет Eliza Abdillabekova
print("Привет " + name + lastname + "мне " + (age) +"лет" )

#задание 3
price = int(input("Введите цену: "))
if price >5000:
    print(f"Доставка {0} рублей")
elif price <=1000:
    print(f"Доставка {200} рублей")
else:
    print(f"1000:5000 Доставка  {100} рублей")

#задание 4
grade = int(input("Введите оценку:"))
if grade >60:
    print(f"Вы прошли тест")
elif grade <=60:
    print("Вы провалили тест")

#задание 5
number1 = int(input("Введите целое число: "))
if number1%2==0:
    print("Это четное число")
else:
    print("Это не четное число")


# задание 6        
number = int(input("Введите четное число: "))
if number1%2==0:
    print("Это число без остатка")
else:
    print("Это число с остатком")

text = "Aidana Adilet"
       #0123456789 
print(text[0])
print(text[7])
print(text[1])
print(text[3])
print(text[8])
print(text[9])
print(text[3])
print(text[10])
print(text[4])
print(text[11])
print(text[5])

#1 доп задание
number1 = 5
number2 = 10
print(number1+number2)

#2 доп задание
number1 = 10
number2 = 5
print(number1-number2)

#3 доп задание
number1 = 20
number2 = 5
number3 = 2
print((number1*number2)/number3)

#4 доп задание
x = 10
y = 5
z = 2
print((x+y)*z)

#5 доп задание
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(number1+number2)

#6 доп задание
dollar = int(input("Введите цену: "))
dollar1=0.9
print(dollar*dollar1)

#7 доп задание
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
print((number1*number2*number3)/3)

#8 доп задание
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(number1%number2)

#1
print(10>5)
print(10<5)