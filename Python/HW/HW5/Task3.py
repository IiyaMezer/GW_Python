import clr

board = list(range(1, 10))

def draw(board):
    print('_' * 17)
    for i in range(3):
        print("     |     |")
        print(f"  {board[0 + i * 3]}  |  {board[1 + i * 3]}  |  {board[2 + i * 3]}")
        print("_____|_____|_____")


def turn_input(player_sigh):
    valid = False
    while not valid:
        player_turn = input(f"Куда ставим {player_sigh}?")

        try: player_turn = int(player_turn)
        except:
            print("Некорректный ввод")
            continue

        if player_turn >= 1 and player_turn <= 9 :
            if(str(board[player_turn-1]) not in "X0"):
                board[player_turn - 1] = player_sigh
                valid = True
            else:
                print("Клетка занята")
        else:
            print("Нужно ввести число от 1 до 9")

def win_check(board):
    win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (6,4,2))
    for each in win:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        return False
def main (board):
    count = 0
    win = False
    while not win:
        clr.clrscr()
        draw(board)
        if count % 2 == 0:
            turn_input("X")
        else:
            turn_input("0")
        count += 1
        if count > 4:
            tmp = win_check(board)
            if tmp:
                print(tmp, "You win")
                win = True
                break
        if count == 9 :
            print("draw")
            break
    draw(board)

main(board)