# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
N = int(input('Enter the number (array size): '))
array = [randint(1, 10) for i in range(1, N+1)]
print(f"The array of {N} numbers is set: ", array, end=' ')
print()
X = int(input('Enter the number: '))
closest_number = closest_number1 = closest_number2 = temp_number = array[0]
for item in array:
    if item == X:
        print(f"The element {item} is equal to {X}")
        closest_number = item
        break
    else:
        if abs(item-X) < abs(closest_number-X):
            closest_number = item
print(f"The array number closest in size to {X} is {closest_number}")
