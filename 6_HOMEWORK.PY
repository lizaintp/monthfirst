# #1
# dictionary = {"a" : 300 , "b" : 400}
# dictionary_2 = {"c" : 500 , "d" : 600}
# dictionary.update(dictionary_2)
# print(dictionary)

# #2
# numbers = {"num_1": 1, "num_2": 2, "num_3": 3, "num_100": 100}
# for key in numbers:
#     numbers[key] *= 5
# print(numbers)

# #3
# student = {"name": "Askhat", "age" : 17, "color" : "White"}
# print(student["age"]*2)

# #4
# student = {"name": "Askhat", "age" : 17, "color" : "White"}
# student["age"] = 16 
# print(student)

# #5 
# student = {"name": "Askhat"}
# student["address"] = "Западный Анар"
# print(student)

# #допдз7
# def chatbot():
#     while True:
#         user_input = input("Имя: ")
        
#         if user_input.endswith('!'):
#             print("Успокойся")
#         elif user_input == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Конечно!")
# #доп дз 8
# chatbot()

# def numbers(num):
#     num_dict = num.split()
#     for a in range (len(num_dict)):
#         print(num_dict[a][0],end = '')
# numbers('bye bye')
#9
# def count_words_occurrences(phrase):
#     words = phrase.split()
#     word_counts = {}
#     for word in words:
#         word = word.lower()
#         word = word.strip('.,!?()[]{}":;')

#         if word:
#             word_counts[word] = word_counts.get(word, 0) + 1

#     return word_counts

# input_phrase = "Money, money, money, it’s always sunny, in the richmen’s world"
# result = count_words_occurrences(input_phrase)
# for word, count in result.items():
#     print(f"{word}: {count}")

#10
def is_isogram(word):
    word = word.lower()

    unique_letters = set(word)

    return len(unique_letters) == len(word)

input_word = input("Введите слово: ")
result = is_isogram(input_word)

if result:
    print("Слово является изограммой.")
else:
    print("Слово не является изограммой.")

# #11
# def number(num):
#     a = n[::-1]
#     print(a)

# n = input('Введите число:')
# number(n)