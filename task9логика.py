# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 # вычисление функции  F
#                 # вывод (x, y, z, w), если  F = 1
# 3) Запишем нашу функцию на языке программирования:
# F = (x or y) and not(y == z) and not(w)
# 4) чтобы выводить не полную таблицу истинности, а только те строки, в которых функция равна 1, добавим условие вывода:
# if F:  # то же самое, что "if F == True:"
#   print(x, y, z, w)
# после запуска программы получаем все интересующие нас строки.
# print(f'пример 1')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = (x or y) and not (y == z) and not (w)
#                 if F:
#                     print( x, y, z, w, F)
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             F = not(a or b) and c
#             #if F:
#             print(a, b, c, F)
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             F = not x or not y <= z
#             if F:
#                 print(x, y, z, F)

# for s1 in 0, 1:
#     for s2 in 0, 1:
#         for s3 in 0, 1:
#          F = s1 and not s2 or s3
#         if F:
#          print(s1, s2, s3, F)
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             F= not x == y or z
#             print(x, y, z, F)








