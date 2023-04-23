# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Enter the number (first set size): '))
m = int(input('Enter the number (second set size): '))
first_set = list()
second_set = list()
for i in range(n):
    first_set.append(int(input('Enter any numbers:  ')))
for j in range(m):
    second_set.append(int(input('Enter any numbers:  ')))
print(f"These are two lists: {first_set}, {second_set}")
first_set = set(first_set)
second_set = set(second_set)
print(f"These are two sets: {first_set}, {second_set}")
print(
    f"The sorted intersection of two sets: {sorted(first_set.intersection(second_set))}")
