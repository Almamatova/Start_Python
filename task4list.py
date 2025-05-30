 Create
a = [] # Пустой список
b = list() # Пустой список
a = [1, 1.1, 'a',[1], (1, 1.1), {1,2}, {'a':1}, None,True] # Список в котором: целое; вещественное; строковое; другой список; кортеж; множество; словарь; пустой тип; булевый тип.
a = (1, 2.1, 3) # Раньше я был кортежом
list(a) # [1, 2.1, 3], но 'a' остался кортежом
b = list('abc') # ['a', 'b', 'c']
 Retrive
a = [1, 1.1, 'a']
print(a) # [1, 1.1, 'a']
print([1, 1.1, 'a']) # [1, 1.1, 'a']
a = [1, 1.1, 'a']
a[0]  # 1
a[1]  # 1.1
a[2]  # 'a'
a[3]  # Ошибка, вышли за границы
a[-1]  # 'a'
a[-2]  # 1.1
a[-3]  # 1
a[-4]  # Ошибка, вышли за границы
a[1, 2, 3,]  #
a.index(3)  # 2. Возвращает индекс, где передаваемое значение стоит в списке. В примере вернется 2, так как значение 3 в списке стоит на 2-ом индексе.
 Update
a = [1, 1.1, 'a']
a[0] = 'a' # Теперь 'a' равно ['a', 1.1, 'a']
a[1] = 'б'# Теперь 'a' равно ['a','б','в']
a[-1] = 'в' # Теперь 'a' равно ['a','б','в']
a[1,2,3] # Теперь 'a' равно [1,2,3]
a[1,2,3]
a.append(4) # Добавляет значение (объект) в конец списка. Добавляет только один объект или значение. Теперь "а" a[1,2,3,4]
a.append(['a','b']) # Теперь "а" [1,2,3,4['a','b']]. Не забываем, что методы в списке изменяют значения и структуру в самом списке.
a[1,2,3]
a.insert(0,4) # Добавляет значение (объект), что стоит на втором месте (4) на место под индексом, что стоит на первом месте(0). В конкретном примере добавиь 4 на 0-ой индекс, т.е. вначало. Теперь "а" [4,1,2,3]
a[1,2,3]
a.insert(3,4) # В конкретном примере добавит 4 на 3-ий индекс, т.е. вконец. Теперь "а" [1,2,3,4]
a[1,2,3]
a.insert(-1,4) # Кажется, что здесь должно зхначение 4 добавиться в конец, но на самом деле 4 встанет в предпоследнеее место. Теперь "а" [1,2,4,3].
a[1,2,3]
a.extend([4, 5, 6]) # Добавляет данные в список поэлементно. Теперь "а" [1,2,3,4, 5, 6]
 Delete
a = [1, 1.1, 'a']
del a[0] # Теперь 'a' равно [1.1,'a']
del a[-1] #  Теперь 'a' равно [1.1]
del a[-1] #  Теперь 'a' равно []
del a # Полное удаление переменной "а"
a = [1,2,3]
a.clear() # Полностью очищает список, превращая его в пустой список. Теперь "а" []
a = [1,2,3]
a.pop() # Возвращает последний элемент и удаляет его из списка. В примере вернет 3 и удалит его из списка. Теперь "а" [1,2]
a = [1,'ab',3]
a.pop(1) # Возвращает элемент по указонному ИНДЕКСУ уи удаляет его из списка. В примере вернет 'ab' и удаляет его из списка. Теперь "а"[1,3]. Если такого индекса нет, то возниенет ошибка.
a = [1,2,'ab']
a.remove('ab') # Удаляет элемент по указанному ЗНАЧЕНИЮ из списка. Если данного значения нет, то появится ошибка.