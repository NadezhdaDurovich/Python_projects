# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:
# 2 2
#     4

from random import randint


def recursive_sum(numb1, numb2):
    if numb1 == 1 or numb2 == 1:
        result = numb2+numb1
        return result
    else:
        result = recursive_sum(numb1+1, numb2-1)
        return result


a = randint(1, 11)
b = randint(1, 11)
print(
    f"The sum of two numbers ({a} and {b}) is equal to {recursive_sum(a,b)}")
