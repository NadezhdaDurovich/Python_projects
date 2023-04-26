# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def raise_to_a_power(numb1, numb2):
    if numb2 == 1:
        raise_result = numb1
        return raise_result
    else:
        raise_result = numb1*raise_to_a_power(numb1, numb2-1)
        return raise_result


A = int(input('Enter the number:'))
B = int(input('Enter the power of number: '))

print(
    f"The result of raising a number {A} to a power {B} is {raise_to_a_power(A, B)}")
