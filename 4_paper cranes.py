# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# # Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# # если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# # *Пример:*
# # 6 -> 1  4  1
# # 24 -> 4  16  4
# # 60 -> 10  40  10

# # вариант №1
petr_paper_cranes = int(
    input('Введите кол-во журавликов, которые Петя изготовил из бумаги: '))
serg_paper_cranes = petr_paper_cranes
kate_paper_cranes = (petr_paper_cranes+serg_paper_cranes)*2
all_paper_cranes = petr_paper_cranes+serg_paper_cranes+kate_paper_cranes
print(f" Всего ребята изготовили {all_paper_cranes} бумажных журавликов")
print(
    f" Петя и Сережа сделали по {petr_paper_cranes} шт.,а Катя целых {kate_paper_cranes} шт.!")

# вариант №2
all_paper_cranes = int(
    input('Введите общее кол-во журавликов, которые ребята изготовили из бумаги: '))
petr_paper_cranes = all_paper_cranes//6
serg_paper_cranes = petr_paper_cranes
kate_paper_cranes = (petr_paper_cranes+serg_paper_cranes)*2
print(
    f" Петя и Сережа сделали по {petr_paper_cranes} шт.,а Катя целых {kate_paper_cranes} шт.!")
