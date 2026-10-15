def print_board(board):
    """Prints the current state of the board in a 3x3 grid layout."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    """Checks if the specified player has won the game."""
    # Predefined winning combinations (rows, columns, diagonals)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def tic_tac_toe():
    """Main game loop managing turns, inputs, and win/tie validation."""
    # Initialize the board with position numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves_played = 0

    print("Welcome to Tic-Tac-Toe!")
    print("Players will take turns entering a position number (1-9).")

    while moves_played < 9:
        print_board(board)
        
        # Get and validate input
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Convert 1-9 choice to 0-8 list index
        index = choice - 1

        if index < 0 or index > 8:
            print("Out of range! Please choose a number from 1 to 9.")
            continue
        
        if board[index] in ["X", "O"]:
            print("That position is already taken! Try another one.")
            continue

        # Place the player's move on the board
        board[index] = current_player
        moves_played += 1

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            return

        # Toggle player turn
        current_player = "O" if current_player == "X" else "X"

    # If the loop finishes without a return, it's a tie
    print_board(board)
    print("It's a draw! Well played.")


if __name__ == "__main__":
    tic_tac_toe()
