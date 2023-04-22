# # ДЗ по теме Циклы (for, while)

# # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# # а некоторые – гербом. Определите минимальное число монеток, которые нужно
# # перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# # Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите общее кол-во монет: '))
amount_of_heads = 0
amount_of_tails = 0
tails = 1
heads = 0
for coin in range(1, n+1):
    coin = input(f"Введите орёл ({heads}) или решка ({tails}): ")
    if coin == '0':
        amount_of_heads += 1
    if coin == '1':
        amount_of_tails += 1
if amount_of_tails < amount_of_heads:
    print(
        f"Достаточно перевернуть {amount_of_tails} монет(ы/y), и везде будет орел")
elif amount_of_tails == amount_of_heads:
    print(f"Неважно, орел или решка - переверните {amount_of_tails} монет(ы)")
else:
    print(
        f"Достаточно перевернуть {amount_of_heads} монет(ы/у), и везде будет решка")
