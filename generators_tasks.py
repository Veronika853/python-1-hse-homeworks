print('''6. На входе строка со словами, разделенными через 1 пробел. 
Найти все слова, длина которых не больше 5. # split, len''')
string = 'один два три четыре пять'
result = [i for i in string.split() if len(i) <= 5]
print('Ответ:')
print(result)
print()


print('''7. На входе строка со словами, разделенными через 1 пробел. 
Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.''')
new = string.split()
result = {i: len(str(i)) for i in new}
print('Ответ:')
print(result)
print()


print('''8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита.
Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.''')
latin_string = 'The quick brown fox jumps over the lazy dog'
result = list({i for i in latin_string})
print('Ответ:')
print(result)
print()


print('''9. На входе список чисел, получить список квадратов этих чисел / use map''')
numbers = [1, 5, 60, 10, 12, 15, 965]
result = list(map(lambda x: x ** 2, numbers))
print('Ответ:')
print(result)
print()


print('''10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. 
Найти все точки, которые принадлежат прямой y = 5 * x - 2.
На выходе получить словарь из самой точки и расстояния до этой точки из начала координат (0, 0)''')
coords = [(1, 1), (2, 3), (5, 3), (1, 3), (-1,  -7)]
result = {i: (i[0]**2 + i[1]**2)**0.5   for i in coords if i[1] == 5 * i[0] - 2}
print('Ответ:')
print(result)
print()


print('''11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.''')
result = [i**2 for i in range(2, 28) if i % 2 == 0]
print(result)
print('Ответ:')
print()


print('''12. На входе список из координат точек на плоскости. 
Найти расстояние до самой удаленной точки от начала координат (0, 0) в первой четверти. # max()''')
coords = [(1, 1), (2, 3), (5, 3), (1, 3), (-1,  -7), (-2, 5), (6, -10)]
result = max([(i[0]**2 + i[1]**2)**0.5 for i in coords if i[0] > 0 and i[1] > 0])
print('Ответ:')
print(result)
print()


print('''13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. 
Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...] 
# list(map(..., nums_first, nums_second))''')
nums_first = [1, 2, 3, 5, 8] 
nums_second = [2, 4, 8, 16, 32]
result = list(map(lambda first,second: (first + second, first - second), nums_first, nums_second))
print('Ответ:')
print(result)
print()


print('''14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. 
Найти четные квадраты этих чисел. 
Ответ записать снова в список из строк, то есть сформировать обратно список строк, 
но уже отфильтровать все четные квадраты.
# print(list(map(int, "1 2 3".split())))''')
string_numbers = ['43141', '32441', '431', '4154', '43121']
result = [int(i)**2 for i in string_numbers if int(i)**2 % 2 == 0]
print('Ответ:')
print(result)
print()


print('''15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит # slice, split, map, zip
```
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""
```

Мы хотим получить нормальную таблицу, чтобы импортировать в csv
```
[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]
```
''')
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

rows = input_str.split('\n')
headers = [i.split(',')[0] for i in rows]
values = [i.split(',')[1:] for i in rows]
data = [dict(zip(headers, [k[i] for k in values])) for i in range(len(headers))]
text = str(data)
formatted_data = text.replace('{', '\n  {\n    ').                 replace(',', ',\n   ').replace('},\n', '\n  },').                 replace('}]', '\n  }\n]').replace("'", '"')
print('Ответ:')
print(formatted_data)
print()


print('''16. Получить сумму по столбцам у двумерного списка # sum, zip''')
a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
result = [sum(i) for i in zip(*a)]
print('Ответ:')
print(result)

