import random

def print_game_board(board):
    x = 0
    for row in board:
        x += 1
        print(" | ".join(row))
        if x <= 2:
            print("-" * 9)

def player_move(symbol, board):
    while True:
        row, col = input("Select a row and a column: ").split()
        row = int(row) - 1
        col = int(col) - 1
        if row > 2 or col > 2:
            print("Wrong field, choose the correct one.")
        elif board[row][col] == " ":
            board[row][col] = symbol
            break
        else:
            print("Field occupied, select another one.")

def computer_move(board, symbol):
    empty_field = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty_field)
    board[row][col] = symbol


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

def check_draw(board):
    is_draw = all(cell != " " for row in board for cell in row)
    if is_draw:
        return True
    else:
        return False

def game():
    print("Welcome to the game of tic-tac-toe!")
    mode = input("Select the game mode 1 - two people, 2 - with the computer")
    game_board = [[" " for _ in range(3)] for _ in range(3)]
    player_symbol = "X"

    while True:
        print_game_board(game_board)
        if mode == "1" or (mode == "2" and player_symbol == "X"):
            player_move(player_symbol, game_board)
        else:
            computer_move(game_board, player_symbol)

        winner = check_win(game_board)
        if winner:
            print(f"You win! {player_symbol}")
            print_game_board(game_board)
            break

        draw = check_draw(game_board)
        if draw:
            print("Draw!")
            print_game_board(game_board)
            break

        print("\n")
        player_symbol = "O" if player_symbol == "X" else "X"





if __name__ == "__main__":
    game()