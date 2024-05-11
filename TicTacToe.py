from tkinter import *
import random

def find_best_move():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                buttons[row][col]["text"] = "O"
                if check_winner("O"):
                    buttons[row][col]["text"] = ""
                    return (row, col)
                buttons[row][col]["text"] = ""

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                buttons[row][col]["text"] = "X"
                if check_winner("X"):
                    buttons[row][col]["text"] = ""
                    return (row, col)
                buttons[row][col]["text"] = ""

    if buttons[1][1]["text"] == "":
        return (1, 1)

    for i in [0, 2]:
        for j in [0, 2]:
            if buttons[i][j]["text"] == "":
                return (i, j)

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return (i, j)
            
def ai_turn():
    row, col = find_best_move()
    buttons[row][col]["text"] = "O"
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
            ai_turn()

def check_winner(player):
    for i in range(3):
        if all(buttons[i][j]["text"] == player for j in range(3)) or all(buttons[j][i]["text"] == player for j in range(3)):
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player or buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:
        return True
    return False

def is_board_full():
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

def new_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
    label.config(text="X's turn")


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
window.minsize(500, 500)  # Set minimum window size
x = (screen_width / 2) - (700 / 2) 
y = (screen_height / 2) - (800 / 2) 
window.geometry(f'+{int(x)}+{int(y)}')

label = Label(window, text="X's turn", font=(FONT, FONT_SIZE * 2), fg=FG_COLOR, bg=BG_COLOR)
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
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j].bind("<Enter>", lambda e, button=buttons[i][j]: on_enter(e, button))
        buttons[i][j].bind("<Leave>", lambda e, button=buttons[i][j]: on_leave(e, button))

# Adjust padding around buttons
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, padx=10, pady=10)


new_game()
window.mainloop()