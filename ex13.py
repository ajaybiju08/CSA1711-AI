def is_moves_left(board):
    """Returns True if there are empty spots remaining on the board."""
    for row in board:
        if '_' in row:
            return True
    return False

def evaluate(board):
    """Evaluates the board state and returns a score based on who won."""
    # Check rows for victory
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == 'O': return 10
            elif board[row][0] == 'X': return -10

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 'O': return 10
            elif board[0][col] == 'X': return -10

    # Check diagonals for victory
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'O': return 10
        elif board[0][0] == 'X': return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'O': return 10
        elif board[0][2] == 'X': return -10

    # Return 0 if nobody has won yet
    return 0

def minimax(board, depth, is_max):
    """The core Minimax recursive function."""
    score = evaluate(board)

    # Base Cases: Return score if game is over
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    # Maximizer's turn (AI)
    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'  # Make temporary move
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'  # Undo move (backtrack)
        return best

    # Minimizer's turn (Human)
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'  # Make temporary move
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'  # Undo move (backtrack)
        return best

def find_best_move(board):
    """Evaluates all possible moves and returns the optimal move for the AI."""
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# --- Example Evaluation ---
# '_' represents an empty space
board = [
    ['X', '_', 'O'],
    ['_', 'X', '_'],
    ['_', '_', '_']
]

print("Current Board State:")
print_board(board)

best_move = find_best_move(board)
print(f"The optimal move for AI ('O') is: Row {best_move[0]}, Column {best_move[1]}")
