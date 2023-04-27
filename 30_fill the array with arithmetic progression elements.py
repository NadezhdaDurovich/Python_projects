# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_element = int(input('Enter the first element of progression: '))
amount_of_elements = int(input('Enter the amount of elements: '))
difference_of_arithmetic_progression = int(
    input('Enter the difference of arithmetic progression: '))

# arithmetic_progression = list()
# for i in range(1, amount_of_elements+1):
#     next_element = first_element+(i-1)*difference_of_arithmetic_progression
#     arithmetic_progression.append(next_element)
# print(f"The result is an arithmetic progression: {arithmetic_progression}")

for i in range(amount_of_elements):
    print(first_element+i*difference_of_arithmetic_progression)
