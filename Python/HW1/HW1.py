import os

def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

def QuarterByPoint():
    clrscr()
    x,y= input('Введите через запятую координаты X и Y: ').split(',')
    x = float(x)
    y = float(y)

    if x > 0 and y > 0:
        print('I четверть')
    elif x > 0 and y < 0:
        print('IV четверть')
    elif x < 0 and y > 0:
        print('II четверть')
    elif x < 0 and y < 0:
        print('III четверть')
    elif x == 0 or y==0:
        print('Точка лежит на оси')

def RangeBySquare():
    clrscr()
    while True:
        Q= input('Введите четверть римской цифрой:')
        match Q:
            case 'I':
                print('Диапазон координат: х>0 , y>0')
                break
            case 'II':
                print('Диапазон координат: х<0 , y>0')
                break
            case 'III':
                print('Диапазон координат: х<0 , y<0')
                break
            case 'IV':
                print('Диапазон координат: х>0 , y<0')
                break
            case _:
                print('Невереный ввод')

def LenghtByPoint():
    clrscr()
    x1,y1,z1= input('Введите через запятую координаты первой точки X,Y,Z: ').split(',')
    x2,y2,z2= input('Введите через запятую координаты второй точки X,Y,Z: ').split(',')

    x1 = float(x1)
    y1 = float(y1)
    z1 = float(z1)

    x2 = float(x2)
    y2 = float(y2)
    z2 = float(z2)

    l = float(((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5)
    print(f'Расстояние равно: {l}')


while True:
    clrscr()
    print('Список заданий')
    print('1.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У')
    print('2.Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти')
    print('3.Найти расстояние между двумя точками пространства')
    print('0.Завершить работу')
    print('-----------------------------------------------------------------------------------------------------------------------')
    task =input('Выберите задание: ')

    match task:
        case '1':
            QuarterByPoint()
        case '2':
            RangeBySquare()
        case '3':
            LenghtByPoint()
        case '0':
            print('Звершение работы...')
            break
        case _:
            print('Неизветсная команда')





