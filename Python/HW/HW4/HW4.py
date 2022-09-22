import Utils.clr as c
import os
import random as R

def prime_factors(n):
    PM=list()
    d=2
    while (d <= n):
        if(n % d) == 0:
            PM.append(d)
            n=n/d
        else:
            d +=1
    return PM

def get_uniq_elements (A):
    UniqueList=list()
    for i in A:
        if A[i] in UniqueList:
            continue
        else:
           UniqueList.append(A[i])
    return UniqueList

def generate_polynome (k):
    Polynome = list ()
    i=k
    while i >= 0:
        n=R.randint(0,100)
        if n==0:
            i -=1
            continue
        else:
            if i == 0:
                Polynome.append((f'{n}'))
            elif i ==1:
                Polynome.append((f'{n}*x+'))
            else:
                Polynome.append((f'{n}*x^{i}+'))
            i -=1
    return Polynome




def Task1():
    c.clrscr()
    n = int(input("Введите целое число для разложения его на простыe множители: "))
    print(f"Простые множители для {n} : {prime_factors(n)}")

def Task2():
    c.clrscr()
    N = 15
    my_list= [None]*N
    for i in range(len(my_list)):
        my_list[i]= R.randint(0, 10) #Специально обьявил массив из 15 элементов, а пределы генерации числа до 10, чтобы получить гарантированно повторяющиеся значения.
    print (f"Исходный массив: {my_list}")
    print (f"Только уникальные элементы массива: {get_uniq_elements(my_list)}")



def Task3():
    c.clrscr()
    num =int(input('Введите k: '))
    Poly ="".join(generate_polynome(num))
    print(f'Сгенерированный полином:{Poly}')
    fn = 'Task03.txt'
    f = open(fn,'w')
    f.write(Poly)
    print(f'Сгенерированный полином записан в файле:{os.path.abspath(fn)}')
    f.close







while True:
    c.clrscr()
    print('Список заданий')
    print('1.Разложение на простые множители')
    print('2.Уникальные элементы массива')
    print('3.Многочлен степени k')
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