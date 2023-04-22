# # Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# # если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку
# # на два прямоугольника).
# # *Пример:*
# # 3 2 4 -> yes
# # 3 2 1 -> no

n = int(input('Enter the width of chocolate bar:'))
m = int(input('Enter the length of chocolate bar:'))
print(f'There is a chocolate bar size ({n} x {m})')
k = int(input('Enter the desired number of chocolate slices:'))
if k < m*n and (k % n == 0 or k % m == 0):
    print(
        f'You can easily break off {k} slices from this chocolate bar with the specified method')

else:
    print(
        f'It is impossible to break off {k} slices from this chocolate bar with the specified method')
