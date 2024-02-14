#1
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
try:
    number1 / number2
    print(number1/number2)
    if number2 == 0:
        print()
except :
    print("На ноль делить нельзя")

#2
name = input("Введите имя: ")
print(name)
if '' in name:
    print("Ошибка")

#3
my_password = [ "12345678"]
user_input = input("Введите пароль: ")
access = "разрешен" if user_input in my_password else "запрещен"
print("Вход " +  access)

#4
try:
    num = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(num+num2)
except ValueError :
    print("ошибка")


#5
def sums(*args):
    numbers = sum(args)
    print(numbers)
sums(2,3,5)


#1Удвоение числа:
result = lambda num2: num2 *2
print(result(5))


#2
numu = lambda num1: num1 %2==0
print(numu(10))

#3
result = lambda num2: num2 **2
print(result(5))

#4
num = ["Kudbuhon","Aslan","Daiyrbek","Eliza"]
result = sorted(num, key=lambda num1: len(num1))
print(result)

#5
con = lambda s,char:char in s
print(con("Liza", "i"))

con = lambda str1, str2: str1+str2
print(con("Hello ","Eliza"))

filtr = lambda numbers  :list(filter(lambda i: i>0, numbers))
numbers = [-3, -2, -1, 0, 1, 2, 3]
print(filtr(numbers))