def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Vodoravno
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Okomito
        [0, 4, 8], [2, 4, 6]  # Dijagonalno
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def is_board_full(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Igrač {current_player} je na potezu.")
        
        while True:
            try:
                move = int(input("Unesite broj polja (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Molimo unesite broj između 1 i 9.")
                elif board[move] != " ":
                    print("To polje je već zauzeto. Odaberite drugo.")
                else:
                    break
            except ValueError:
                print("Molimo unesite validan broj.")
        
        board[move] = current_player
        
        if check_win(board):
            print_board(board)
            print(f"Igrač {current_player} je pobijedio!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Igra je završila neriješeno!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Dobrodošli u igru Križić-kružić!")
    play_game()

input("Pritisnite Enter za izlaz...")