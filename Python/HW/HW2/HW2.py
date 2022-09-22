import Utils.clr as c
import random


def factorial(n: int):
    res: int = 1
    for i in range(1, n + 1):
        res *= i
        print(res, end = '; ')


def Task1():
    c.clrscr()
    # Разделяем дробное число на чписок из двух элментов
    a = list(map(int, input('Введите число, десячисную часть сделует разделить запятой: ').split(',')))

    a = a[0]
    b = a[1]

    i: int = 0
    while a != 0:  # складываем цифры целой части
        i = i + (a % 10)
        a = a // 10

    while b != 0:  # складываем цифры дробной части
        i = i + (b % 10)
        b = b // 10
    print("Произведение цифр равно:", i)


def Task2():
    c.clrscr()
    n = int(input('Введите n: '))
    factorial(n)


def Task3():
    c.clrscr()
    n = int(input('Введите n: '))
    a = [i for i in range(1,n+1)]
    print(f'Массив до перетасовки: {a}')
    if len(a) > 1:
        i = len(a) - 1
        while i > 0:
            rep = random.randint(0, i)
            a[i], a[rep] = a[rep], a[i]
            i -= 1
    print(f'Массив после перетасовки: {a}')


while True:
    c.clrscr()
    print('Список заданий')
    print('1.Сумма цифр в числе')
    print('2.Факториал по порядку')
    print('3.Перемешивание списка')
    print('0.Завершить работу')
    print(
        "-----------------------------------------------------------------------------------------------------------------------"
    )
    task = input('Выберите задание: ')

    match task:
        case '1':
            Task1()
        case '2':
            Task2()
        case '3':
            Task3()
        case '0':
            print('Звершение работы...')
            break
        case _:
            print('Неизветсная команда')
