# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# # и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# # где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 –
# # счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# # счастливость билета.
# # *Пример:*
# # 385916 -> yes
# # 123456 -> no

print('Let\'s check your ticket...')
ticket_number = str(input('Enter the six-digit number of your ticket: '))
if (int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])) == (int(ticket_number[3]) +
                                                                           int(ticket_number[4])+int(ticket_number[5])):
    print('Yes, this ticket is a lucky one!')
else:
    print('No, this ticket is ordinary')
