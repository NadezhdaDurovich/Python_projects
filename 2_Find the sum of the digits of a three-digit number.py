# ДЗ по теме "Ввод-Вывод, операторы ветвления"

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
number = int(input('Введите любое трехзначное число: '))
if number // 100 == 0 or number//1000!=0:
    print('Число должно быть трехзначным, попробуйте еще раз:)')
else:
    units = number % 10
    dozens = (number % 100-units)//10
    hundreds = number // 100
    print(f"Сумма цифр числа {number} равна {hundreds+dozens+units}")
