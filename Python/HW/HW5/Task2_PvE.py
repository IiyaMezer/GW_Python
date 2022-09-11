import clr
from random import randint
clr.clrscr()


def set_max_candy(x, y):
    if x < y:
        y = x
    return y


СANDY = int(2021)  # начальное значение конфет

candy_current = СANDY
the_last_turn = 0  # Переменная для определения последнего игрока

max_candy_per_turn = int(28)
while candy_current > 0:
    p_one_turn = int(
        input(f"Игрок 1, сколько конфет хотите забрать?(0...{set_max_candy(candy_current, max_candy_per_turn)})"))
    candy_current -= p_one_turn
    print(f"Конфет осталось: {candy_current}")
    the_last_turn = 1

    if candy_current == 0:
        break
    # bot_turn = randint(1, set_max_candy(candy_current, max_candy_per_turn))
    bot_turn = candy_current % (set_max_candy(candy_current, max_candy_per_turn)+1)
    if bot_turn == 0:
        bot_turn = 1
    candy_current -= bot_turn
    print(f"Бот забирает {bot_turn} конфет")
    print(f"Конфет осталось: {candy_current}")
    the_last_turn = 2

if the_last_turn == 1:
    print("Игрок выиграл.")
else:
    print("Бот выиграл.")