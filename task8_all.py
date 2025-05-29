# for value in collection: # Начало блока кода с телом цикла
#     ...
#     # Конец блока кода с телом цикла
#     # Код, который будет выполняться после цикла
# for i in range(3)
#     print(i+1, "шаг цикла") # будет выполнено 3 раза
# print("Первый цикл закончился!")
# a = {1: 'x', 2: 'y', 3: 'z'}
# for index, value in a.items():
#     print(f'"Позиция: {index}-> Значение: {value }"')
# range(10) # Генерация последовательности чисел от 0 до 9
# range(1, 11) # Генерация последовательности чисел от 1 до 10
# range(1, 11, 2) # Генерация последовательности чисел от 1 до 10 с шагом 2
# range(10, 0, -1) # Генерация последовательности чисел от 10 до 1 с шагом -1
# for tuple_ in enumerate(["а", "б", "в"]):
#     print(tuple_)
# for pos, value in enumerate("абв", start=1): # start можно укуазать любым целым числом
#     print("Позиция:", pos,"->", "Значение:", value)
#
# numbers = (10, 20, 30, 40, 50) # Объявление списка чисел
# total = 0 # TODO Заменить использование индексов на перебор значений списка
# for i in range(len(numbers)):
#     total +=numbers[i]
# print("Сумма чисел:", total) # Сумма чисел: 150
# count = 0
# while count < 5:
#     print("Значение count:", count)
#     count += 1
# sum_ = 0
# input_number = int(input("Введите число:"))
# while input_number != 0:
#     sum_ += input_number
#     input_number = int(input("Введите число:"))
# print("Ответ:", sum_)

# a, s, p = 1, 150, 200
# while True:
#     if a>10:
#         break
#     a += 2
#     p += a
#     s += p
# print(s)
# c, d = 750, 90
# while True:
#     if d>0:
#         break
#     d -= 10
#     c = c/2 + 50
# print(c)
# s = 1
# for n in range(1,6):
#     s *= n
# print(s)
# m, n = 12, 5
# while True:
#     if m == n:
#      break
#     elif m > n:
#         m -= 2 * n
#     else:
#         n -=3
# print(m)

# print(f'Задакча 3 b множественные условия')
# m, n = 12, 5
# while m != n:
#     if m>n:
#         m -= 2 * n
#     else:
#         n -= 3
# print(f'переменная m = {m}')
