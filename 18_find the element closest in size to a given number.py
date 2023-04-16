# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
N = int(input('Enter the number (array size): '))
array = [i for i in range(1, N+1)]
print(f"The array of {N} numbers is set: ", array, end=' ')
print()
X = int(input('Enter the number: '))
min_value = array[0]
for item in array:
    if item == X:
        print(f"The number {item} is equal to the specified value {X}.")
    else:
        if abs(item-X) < abs(min_value-X):
            min_value = array[item]
            print(f"The array number closest in size to {X} is {min_value}")
        # else:
        #     print(f"The array number closest in size to {X} is {min_value}")
