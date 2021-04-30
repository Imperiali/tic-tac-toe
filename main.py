theBoard = dict([(idx, ' ') for idx in range(1, 10)])

victories = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 5, 9),
    (7, 5, 3),
]


def print_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("-"*9)
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("-"*9)
    print(f"{board[3]} | {board[2]} | {board[1]}")


def has_finished(board):
    return all([value != " " for value in board.values()])


def check_sequency(positions):
    i, j, h = positions
    if theBoard[i] == theBoard[j] == theBoard[h] != " ":
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
    while not has_finished(theBoard):
        # Inicia a vez
        print()
        print(f"Jogador {turn} é a sua vez")
        try:
            move = int(input("Qual posição de sua jogada? "))
        except:
            print("Posição invalida")
            continue

        if theBoard[move] == " ":
            theBoard[move] = turn
        else:
            print("Posição já jogada")
            continue

        print(print_board(theBoard))

        if has_winner():
            print_end_game(turn)
            return

        # Alterna as rodadas
        if turn == "X":
            turn = "O"
        else:
            turn = "X"


if __name__ == "__main__":
    game()
