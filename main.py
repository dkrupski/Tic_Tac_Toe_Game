import random

game_board = [[" " for _ in range(3)] for _ in range(3)]


def player_move(symbol):
    while True:
        player_row = int(input("Select a row: ")) - 1
        player_col = int(input("Select a column: ")) - 1
        if game_board[player_row][player_col] == " ":
            game_board[player_row][player_col] = symbol
            break
        else:
            print("Field occupied, select another one.")


def print_game_board():
    x = 0
    for row in game_board:
        x += 1
        print(" | ".join(row))
        if x <= 2:
            print("-" * 9)

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return None


while True:
    player_symbol = "X"
    player_move(player_symbol)
    print_game_board()
    winner = check_win(game_board)
    if winner:
        print("You win!")
        break



    player_symbol = "O"
    player_move(player_symbol)
    print_game_board()
    winner = check_win(game_board)
    if winner:
        print("You win!")
        break


