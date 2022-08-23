import clr as c
import random


def Task1():
    c.clrscr()
    A = list(map(int, input('Введите числа через запятую: ').split(',')))
    Summ=0 
    for i in range(len(A)): 
        if A[i]%2!=0: 
            Summ=Summ+A[i] 
    print(f'Сумма нечетных элементов массива: {Summ}')


def Task2():
    c.clrscr()
    N =int(input('Введите N: '))
    factorial(N)

def Task3():
    c.clrscr()
    N =int(input('Введите N: '))
    A= [None]*N
    for i in range(len(A)):
        A[i]= i
    print(f'Массив до перетасовки: {A}')
    if len(A) > 1:
       i = len(A) - 1
       while i > 0:
           rep = random.randint(0, i)
           A[i], A[rep] = A[rep], A[i]
           i -= 1
    print(f'Массив после перетасовки: {A}')



while True:
    c.clrscr()
    print('Список заданий')
    print('1.Сумма нечетных элементов массива')
    print('2.Факториал по порядку')
    print('3.Перемешивание списка')
    print('0.Завершить работу')
    print('-----------------------------------------------------------------------------------------------------------------------')
    task =input('Выберите задание: ')

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


