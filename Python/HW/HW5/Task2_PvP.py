import clr
clr.clrscr()

def set_max_candy(x, y):
    if x < y:
        y = x
    return y


СANDY = int(2021)  # начальное значение конфет

candy_current = СANDY
the_last_turn = 0  # Переменная для определния последнего игрока

max_candy_per_turn = int(28)
while candy_current > 0:
    p_one_turn = int(
        input(f"Игрок 1, сколько конфет хотите забрать?(1...{set_max_candy(candy_current, max_candy_per_turn)})"))
    candy_current -= p_one_turn
    print(f"Конфет осталось: {candy_current}")
    the_last_turn = 1

    if candy_current == 0:
        break
    p_two_turn = int(
        input(f"Игрок 2, сколько конфет хотите забрать?(1...{set_max_candy(candy_current, max_candy_per_turn)})"))
    candy_current -= p_two_turn
    print(f"Конфет осталось: {candy_current}")
    the_last_turn = 2

if the_last_turn == 1:
    print("Игрок 1 выиграл.")
else:
    print("Игрок 2 выиграл.")
