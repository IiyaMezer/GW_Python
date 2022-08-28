import clr as c
import random

def PrimeFactors(n):
    PM=list()       #PrimeFactors
    d=2
    while (d <= n):
        if(n % d) == 0:
            PM.append(d)
            n=n/d
        else:
            d +=1
    return PM

def GetUniqElements (A):
    UniqueList=list()
    for i in A:
        if A[i] in UniqueList:
            continue
        else:
           UniqueList.append(A[i])
    return UniqueList



def Task1():
    c.clrscr()
    n = int(input("Введите целое число для разложения его на простыe множители: "))
    print(f"Простые множители для {n} : {PrimeFactors(n)}")

def Task2():
    c.clrscr()
    N = 15
    A= [None]*N
    for i in range(len(A)):
        A[i]= random.randint(0, 10) #Специально обьявил массив из 15 элементов, а пределы генерации числа до 10, чтобы получить гарантированно повторяющиеся значения.
    print (f"Исходный массив: {A}")
    print (f"Только уникальные элементы массива: {GetUniqElements(A)}")



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
    print('1.Разложение на простые множители')
    print('2.Уникальные элементы массива')
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