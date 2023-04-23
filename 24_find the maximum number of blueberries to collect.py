# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
bushes = int(input('Enter the number of bushes: '))
blueberries = [randint(1, 21) for i in range(bushes)]
print(f"Total ripe blueberries {blueberries}")
maxsum = 0
best_bush = 0
for i in range(1, bushes-1):
    cursum = sum(blueberries[i-1:i+2])
    print(f"berries on {i},{i+1},{i+2} bushes - {cursum}")
    if cursum > maxsum:
        maxsum = cursum
        best_bush = i+1
cursum1 = blueberries[-1]+blueberries[-2]+blueberries[0]
print(f"berries on {bushes-1},{bushes} and 1 bushes -{cursum1}")
cursum2 = blueberries[0]+blueberries[-1]+blueberries[1]
print(f"berries on {bushes}, 1 and 2 bushes -{cursum2}")
if cursum1 > maxsum:
    maxsum = cursum1
    best_bush = bushes
if cursum2 > maxsum:
    maxsum = cursum2
    best_bush = 1
print(
    f"The maximum number of berries ({maxsum}) the module can collect near the bush {best_bush}")
