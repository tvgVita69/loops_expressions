name = None  # вначале мы не знаем имени пользователя

# бесконечный цикл
while True:
    print('Меню:')
    print('1. Ввести имя')
    print('2. Вывести приветствие')
    print('3. Выйти')
    response = input('Выберите пункт: ')

    print()

    if response == '1':
        name = input('Введите ваше имя: ')
    elif response == '2':
        if name:  # здороваемся с пользователем, если имя уже введено
            print('Привет, ', name, '!', sep='')
        else:
            print('Я не знаю вашего имени.')
    elif response == '3':
        # оператор break завершает выполнение цикла
        break  # если пользователь выбрал третий пункт, то выходим из цикла
    else:
        print('Неверный ввод.')

    print()

*******************************************************************************

# более простой пример
while True:
    print('Введите exit, чтобы завершить цикл')
    response = input('> ')
    if response == 'exit':
        break
