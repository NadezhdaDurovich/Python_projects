def read_file(filename): # показаь все контакты
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            print(line. strip())

def serch_info(filename): # поиск контакта
    request = input('Введите критерий поиска:', end='')
    with open(filename, 'r', encoding='utf-8') as data:
        result = [i for i in data if request in i]
        print(result. strip())

def export(filename): # экспорт контакта
    request = input(
        'Введите критерии для копирования данных в записную кнжку:')
    with open(filename, 'r', encoding='utf-8') as data:
        for i in data:
            if request.upper() in i.upper():
                with open('notebook.txt', 'a') as data1:
                    data1.writelines(i)

def add_data(filename): # добавление контакта
    contact= input('Введите данные нового абонента: ', end=' ')
    with open(filename, 'a') as data:
        data.writelines(contact.split())