# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
n=int(input('Enter the number of array elements: '))
array=[randint(1,10) for i in range (1,n+1)]
print('А random array of elements is set: ',array, end=' ')
print()
x=int(input('Enter the number: '))
counter=0
for item in array:
    if x==item:
        counter+=1
print(f"The number {x} occurs in the array {counter} time(s).")

