# ДЗ к семинару №7.

# Задача 34.
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

def rhyme_search(condition, data):
    number_of_vowels = list(map(condition, data))
    return len(set(number_of_vowels)) == 1


russian_vowels = ['а', 'о', 'и', 'у', 'е', 'ы', 'ё', 'э', 'я', 'ю']


def counting_vowels(object):
    counting_result = 0
    for i in object.lower():
        if i in russian_vowels:
            counting_result += 1
    return counting_result


fraze = [x for x in input().split()]

if rhyme_search(counting_vowels, fraze):
    print('Парам пам-пам')
else:
    print('Пам парам')