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
    A = list(map(int, input('Введите числа через запятую: ').split(',')))
    print('Произведение пар массива: ')
    for i in range(len(A)//2):
        Mult=0
        Mult = A[i]*A[len(A)-1-i]
        print(Mult, end='; ')


def Task3():
    c.clrscr()
    
    A= [1.5,2.13,4.16,5.32]
    print(A)
    Max = 0
    Min = 0
    for i in range(len(A)): #Ищем нибольшую дробную часть
        fValue = 0
        intValue = int(A[i])
        fValue = A[i] - intValue
        if(fValue>Max):
            Max = fValue
    Min=Max
    for i in range(len(A)): #Ищем наменьшую дробную часть
        fValue = 0
        intValue = int(A[i])
        fValue = A[i] - intValue
        if(fValue<Min):
            Min = fValue
    print('Ответ:',round(Max - Min,3))

def Task4():
    c.clrscr()
    A= 16
    print(bin(A))

def Task5():
    c.clrscr()
    A= 16
    print(A)
    Bin = ''
    while A > 0:
        Bin += str(A%2)
        A = A//2
    print(Bin)




while True:
    c.clrscr()
    print('Список заданий')
    print('1.Сумма нечетных элементов массива')
    print('2.Произведение пар чисел массива')
    print('3.Разница между наменьшей и наибольшей дробной частью массива')
    print('4.Из десятичной в дробное')
    print('5.Из десятичной в дробное "руками"')
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
        case '4':
            Task4()
        case '5':
            Task5()
        case '0':
            print('Звершение работы...')
            break
        case _:
            print('Неизветсная команда')


