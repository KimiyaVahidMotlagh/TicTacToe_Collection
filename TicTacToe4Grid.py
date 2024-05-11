from tkinter import *
import math
import json
import time

# Score variables
x_wins = 0
o_wins = 0
ties = 0
def update_scoreboard():
    global x_wins, o_wins, ties
    return f"X Wins: {x_wins} | O Wins: {o_wins} | Ties: {ties}"

# Load and save functions for first_move_responses
def load_moves_from_file():
    try:
        with open("ai_moves.json", "r") as file:
            loaded_moves = json.load(file)
        # Convert string keys back to tuples
        return {eval(key): value for key, value in loaded_moves.items()}
    except FileNotFoundError:
        return {}

def save_moves_to_file():
    # Convert tuple keys to strings
    modified_first_move_responses = {str(key): value for key, value in first_move_responses.items()}
    with open("ai_moves.json", "w") as file:
        json.dump(modified_first_move_responses, file)

# Initialize first_move_responses and load existing data
first_move_responses = load_moves_from_file()

def evaluate_board(board):
    # Checking for Rows for X or O victory.
    for row in range(4):
        if all(board[row][col] == 'O' for col in range(4)):
            return +10
        elif all(board[row][col] == 'X' for col in range(4)):
            return -10

    # Checking for Columns for X or O victory.
    for col in range(4):
        if all(board[row][col] == 'O' for row in range(4)):
            return +10
        elif all(board[row][col] == 'X' for row in range(4)):
            return -10

    # Checking for Diagonals for X or O victory.
    if all(board[i][i] == 'O' for i in range(4)) or all(board[i][3 - i] == 'O' for i in range(4)):
        return +10
    if all(board[i][i] == 'X' for i in range(4)) or all(board[i][3 - i] == 'X' for i in range(4)):
        return -10

    # Else if none of them have won then return 0
    return 0

transposition_table = {}

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    board_key = tuple(tuple(row) for row in board)

    # Check if the board state is already in the transposition table
    if board_key in transposition_table:
        return transposition_table[board_key]

    score = evaluate_board(board)

    # Check for terminal states
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_board_full():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == "":
                    board[i][j] = "O"
                    val = minimax(board, depth + 1, False, alpha, beta)
                    best = max(best, val)
                    alpha = max(alpha, best)
                    board[i][j] = ""
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        transposition_table[board_key] = best
        return best
    else:
        best = math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == "":
                    board[i][j] = "X"
                    val = minimax(board, depth + 1, True, alpha, beta)
                    best = min(best, val)
                    beta = min(beta, best)
                    board[i][j] = ""
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        transposition_table[board_key] = best
        return best

# The rest of your functions like evaluate_board, is_board_full, etc., remain unchanged.

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    alpha = -math.inf
    beta = math.inf

    for i in range(4):
        for j in range(4):
            if board[i][j] == "":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, alpha, beta)  # Using alpha-beta pruning for the first move
                board[i][j] = ""
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break
        if beta <= alpha:
            break

    return best_move

def ai_turn():
    start_time = time.time()  # Start time measurement

    # Convert the current board state to a tuple for use as a dictionary key
    current_board = tuple(tuple(buttons[i][j]["text"] for j in range(4)) for i in range(4))

    # Determine the number of moves made so far to check if it's the first move
    moves_made = sum(row.count('X') + row.count('O') for row in current_board)

    if moves_made == 1 and current_board in first_move_responses:
        # Use the saved move for the first move
        row, col = first_move_responses[current_board]
    else:
        # Calculate the best move using minimax
        board = [[buttons[i][j]["text"] for j in range(4)] for i in range(4)]
        row, col = find_best_move(board)

        # If it's the first move, save this move in the dictionary
        if moves_made == 1:
            first_move_responses[current_board] = (row, col)
            save_moves_to_file()  # Save updated first_move_responses

    end_time = time.time()  # End time measurement
    elapsed_time = end_time - start_time
    print(f"AI turn took {elapsed_time} seconds.")

    # Make the move
    buttons[row][col]["text"] = "O"

    # Check game status
    if check_winner("O"):
        label.config(text="O wins!")
    elif is_board_full():
        label.config(text="Tie!")
    else:
        label.config(text="X's turn")


def next_turn(row, column):
    if buttons[row][column]["text"] == "" and not check_winner("X") and not check_winner("O"):
        buttons[row][column]["text"] = "X"
        if check_winner("X"):
            label.config(text="X wins!")
        elif is_board_full():
            label.config(text="Tie!")
        else:
            label.config(text="O's turn")  # Update label to "O's turn"
            window.after(700, ai_turn)  # 700 milliseconds = 0.7 seconds


def check_winner(player):
    global x_wins, o_wins

    # Check rows and columns for victory
    for i in range(4):
        if all(buttons[i][j]["text"] == player for j in range(4)) or all(buttons[j][i]["text"] == player for j in range(4)):
            if player == "X":
                x_wins += 1
            else:
                o_wins += 1
            update_scoreboard()
            return True

    # Check diagonals for victory
    if all(buttons[i][i]["text"] == player for i in range(4)) or all(buttons[i][3 - i]["text"] == player for i in range(4)):
        if player == "X":
            x_wins += 1
        else:
            o_wins += 1
        update_scoreboard()
        return True

    return False

def is_board_full():
    full = all(buttons[i][j]["text"] != "" for i in range(4) for j in range(4))
    if full:
        global ties
        ties += 1
    return full

def new_game():
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(text="")
    label.config(text="X's turn")

        # Update the scoreboard and label
    scoreboard.config(text=update_scoreboard(), fg=FG_COLOR, bg=BG_COLOR)
    label.config(text="X's turn", fg=FG_COLOR, bg=BG_COLOR)


# Styling constants
BG_COLOR = "#282a36"  # Background color
FG_COLOR = "#f8f8f2"  # Foreground color
BUTTON_COLOR = "#44475a"
BUTTON_HOVER_COLOR = "#6272a4"
FONT = "Verdana"
FONT_SIZE = 20  # Slightly larger
def on_enter(e, button):
    button['background'] = BUTTON_HOVER_COLOR
    button['foreground'] = BG_COLOR  # Change text color
def on_leave(e, button):
    button['background'] = BUTTON_COLOR
    button['foreground'] = FG_COLOR  # Revert text color

# Initialize Tkinter window
window = Tk()
window.title("4x4 Tic-Tac-Toe")
window.configure(bg=BG_COLOR)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.minsize(700, 500)  # Set minimum window size
x = (screen_width / 2) - (700 / 2) 
y = (screen_height / 2) - (800 / 2) 
window.geometry(f'+{int(x)}+{int(y)}')

scoreboard = Label(window, text=update_scoreboard(), font=(FONT, FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
scoreboard.pack(side="top", pady=(10, 0))

label = Label(window, text="X's turn", font=(FONT, FONT_SIZE * 2), fg=FG_COLOR, bg=BG_COLOR)
scoreboard.pack(side="top", fill="x", pady=(10, 5))  # Fill the x-axis for the scoreboard
label.pack(side="top", pady=(5, 20))  # Status label

reset_button = Button(window, text="Restart", font=(FONT, FONT_SIZE), command=new_game, bg=BUTTON_COLOR, fg=FG_COLOR)
reset_button.pack(side="top", pady=10)

frame = Frame(window, bg=BG_COLOR)
# Add padding around the frame
frame.pack(pady=10, padx=10)
# Define buttons in a 4x4 grid
buttons = [[Button(frame, text="", font=(FONT, FONT_SIZE * 2), width=3, height=1,
                    command=lambda row=i, column=j: next_turn(row, column),
                    bg=BUTTON_COLOR, fg=FG_COLOR) for j in range(4)] for i in range(4)]

# Place buttons in the grid and bind hover effects
for i in range(4):
    for j in range(4):
        buttons[i][j].grid(row=i, column=j, padx=10, pady=5)
        buttons[i][j].bind("<Enter>", lambda e, button=buttons[i][j]: on_enter(e, button))
        buttons[i][j].bind("<Leave>", lambda e, button=buttons[i][j]: on_leave(e, button))

# Adjust padding around scoreboard and label
scoreboard.pack(side="top", pady=(10, 0))
label.pack(side="top", pady=(0, 20))

# Adjust padding around buttons
for i in range(4):
    for j in range(4):
        buttons[i][j].grid(row=i, column=j, padx=10, pady=10)


new_game()
window.mainloop()