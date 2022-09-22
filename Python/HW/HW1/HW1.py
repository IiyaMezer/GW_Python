import os

def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

def quarter_py_point():
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

def range_by_square():
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

def lenght_by_point():
    clrscr()
    x1,y1,z1= list(map(int, input('Введите через запятую координаты первой точки X,Y,Z: ').split(',')))
    x2,y2,z2= list(map(int, input('Введите через запятую координаты первой точки X,Y,Z: ').split(',')))
    
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
            quarter_py_point()
        case '2':
            range_by_square()
        case '3':
            lenght_by_point()
        case '0':
            print('Звершение работы...')
            break
        case _:
            print('Неизветсная команда')





