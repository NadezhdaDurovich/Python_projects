# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
N = int(input('Введите любое число: '))
k = 1
n = 2
while (n**k <= N):
    print(n**k, end=' ')
    k += 1
print()
print(
    f"Число {n} в степени {k-1} равное {n**(k-1)} не превышает заданное число {N}")