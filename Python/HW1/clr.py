import os

def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')