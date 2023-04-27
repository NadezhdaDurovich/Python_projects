# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
array_length = int(input('Введите число - размер массива: '))
array = [randint(1, 11) for i in range(array_length)]
print(f"Задан массив {array}")
# вариант 2
min_elem = int(input('Задайте минимальное значение: '))
max_elem = int(input('Задайте максимальное значение: '))
print('Найдем индексы элементов, которые больше min значения, но меньше max значения: ')
# вариант 1
# for j in range(len(array)):
#     if min(array) < array[j] < max(array):
#         print(j, end=' ')
for j in range(len(array)):
    if min_elem < array[j] < max_elem:
        print(j, end=' ')
