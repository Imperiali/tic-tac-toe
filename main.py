THE_BOARD = dict([(idx, ' ') for idx in range(1, 10)])

victories = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 5, 9),
    (7, 5, 3),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
]


def print_board():
    print(f"{THE_BOARD[7]} | {THE_BOARD[8]} | {THE_BOARD[9]}")
    print("-"*9)
    print(f"{THE_BOARD[4]} | {THE_BOARD[5]} | {THE_BOARD[6]}")
    print("-"*9)
    print(f"{THE_BOARD[3]} | {THE_BOARD[2]} | {THE_BOARD[1]}")


def has_finished():
    return all([value != " " for value in THE_BOARD.values()])


def reset_board():
    global THE_BOARD
    for idx in THE_BOARD.keys():
        THE_BOARD[idx] = ' '


def check_sequency(positions):
    i, j, h = positions
    if THE_BOARD[i] == THE_BOARD[j] == THE_BOARD[h] != " ":
        return True
    return False


def print_end_game(player):
    print("*"*15)
    print("\n Fim do Jogo! \n")
    print(f"\n {player} ganhou! \n")
    print("*"*15)


def has_winner():
    return any([check_sequency(p) for p in victories])


def game():
    turn = "X"
    while not has_finished():
        # Inicia a vez
        print()
        print(f"Jogador {turn} é a sua vez")
        try:
            move = int(input("Qual posição de sua jogada? "))
        except:
            print("Posição invalida")
            continue

        if THE_BOARD[move] == " ":
            THE_BOARD[move] = turn
        else:
            print("Posição já jogada")
            continue

        print(print_board())

        if has_winner():
            print_end_game(turn)
            break

        # Alterna as rodadas
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    print_board()
    restart = input("Deseja jogar novamente?(y/n) ")
    if restart == 'y':
        reset_board()


if __name__ == "__main__":
    game()
