#### IMPORTANT BASICS
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()



#### CONSTANTS
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#### WINDOW EDITS
root.title("TicTacToe")

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(window_x) + "+" + str(window_y))

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)



#### FUNCTIONS
def show_frame(frame):
    frame.tkraise()

def play_game():
    reset_game()
    show_frame(game_page)

back_page=None
def help(original_page: str):
    global back_page
    back_page = original_page
    show_frame(help_page)
    
def return_from_help():
    if back_page == "welcome_page":
        show_frame(welcome_page)
    elif back_page=="game_page":
        show_frame(game_page)

def return_home():
    reset_game()
    show_frame(welcome_page)

def choose_shape(shape: str):
    global player_shape
    global computer_shape
    global current_user_turn

    if shape == "X":
        player_shape = "X"
        computer_shape = "O"
    else:
        player_shape = "O"
        computer_shape = "X"

    current_user_turn = True

    shape_selection.grid_remove()
    game_status.configure(text="Your Turn - You are " + player_shape)


def board_click(event):
    global current_user_turn

    if player_shape == None or current_user_turn == False:
        return

    column = event.x // 140
    row = event.y // 140

    if column > 2 or row > 2:
        return

    position = row * 3 + column

    if game_board[position] != "":
        return

    game_board[position] = player_shape
    draw_shape(position, player_shape)

    if check_winner(player_shape):
        end_game("You Win!")
        return

    if check_tie():
        end_game("Tie Game!")
        return

    current_user_turn = False
    game_status.configure(text="Computer's Turn")

    root.after(500, computer_move)


def computer_move():
    global current_user_turn

    available_positions = []

    for i in range(9):
        if game_board[i] == "":
            available_positions.append(i)

    if len(available_positions) == 0:
        return

    position = random.choice(available_positions)

    game_board[position] = computer_shape
    draw_shape(position, computer_shape)

    if check_winner(computer_shape):
        end_game("Computer Wins!")
        return

    if check_tie():
        end_game("Tie Game!")
        return

    current_user_turn = True
    game_status.configure(text="Your Turn - You are " + player_shape)


def draw_shape(position, shape):
    row = position // 3
    column = position % 3

    x = column * 140 + 70
    y = row * 140 + 70

    board.create_text(x, y, text=shape, font=("Verdana", 60, "bold"), tags="shape")


def check_winner(shape):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if game_board[combination[0]] == shape and game_board[combination[1]] == shape and game_board[combination[2]] == shape:
            return True

    return False


def check_tie():
    for position in game_board:
        if position == "":
            return False

    return True


def end_game(message):
    global current_user_turn

    current_user_turn = False
    game_status.configure(text=message)
    play_again_button.grid()


def reset_game():
    global player_shape
    global computer_shape
    global current_user_turn
    global game_board

    player_shape = None
    computer_shape = None
    current_user_turn = None

    game_board = ["", "", "", "", "", "", "", "", ""]

    board.delete("shape")

    game_status.configure(text="")
    play_again_button.grid_remove()
    shape_selection.grid()


def play_again():
    reset_game()



#### WELCOMEPAGE GUI
welcome_page = tk.Frame(root)
welcome_page.configure(background="black")

welcome_page.grid_columnconfigure(0, weight=1)

welcome_page.grid_rowconfigure(0, weight=12)
welcome_page.grid_rowconfigure(1, weight=2)
welcome_page.grid_rowconfigure(2, weight=2)
welcome_page.grid_rowconfigure(3, weight=2)
welcome_page.grid_rowconfigure(4, weight=1)

welcome_page.grid(row=0, column=0, sticky="nsew")

intro_msg = tk.Label(welcome_page, text="Welcome to Tic Tac Toe!")
intro_msg.configure(background="black", foreground="dark blue", font=("Verdana", 40, "bold"))
intro_msg.grid(row=0, column=0)

play_btn = tk.Button(welcome_page, text="Play", command=play_game, background="green", foreground="white")
play_btn.configure(width=20, height=3, font=("Verdana", 12, "bold"))
play_btn.grid(row = 1, column = 0)

help_btn = tk.Button(welcome_page, text="Help", command=lambda:help("welcome_page"))
help_btn.configure(width=16, height=3, font=("Verdana", 12, "bold"))
help_btn.grid(row=2, column=0)

exit_btn = tk.Button(welcome_page, text="Exit Game", command=root.destroy)
exit_btn.configure(width=14, height=3, font=("Verdana", 12, "bold"))
exit_btn.grid(row=3, column = 0)



#### HELPPAGE GUI
help_page = tk.Frame(root)
help_page.configure(background="black")
help_page.grid(row=0, column=0, sticky="nsew")

help_page.grid_columnconfigure(0, weight=1)
help_page.grid_columnconfigure(1, weight=6)
help_page.grid_columnconfigure(2, weight=1)

help_page.grid_rowconfigure(0, weight=1)
help_page.grid_rowconfigure(1, weight=4)
help_page.grid_rowconfigure(2, weight=30)
help_page.grid_rowconfigure(3, weight=4)
help_page.grid_rowconfigure(4, weight=1)

return_btn = tk.Button(help_page, text="Return", command=return_from_help)
return_btn.configure(width=17, height=4, font=("Verdana", 12, "bold"))
return_btn.grid(row=0, column=1)

instructions = tk.Frame(help_page)
instructions.configure(background="black")
instructions.grid(row=2, column=1, sticky="nsew")

instructions.grid_columnconfigure(0, weight=40)
instructions.grid_columnconfigure(1, weight=1)
instructions.grid_columnconfigure(2, weight=40)

instructions.grid_rowconfigure(0, weight=1)

left_page = tk.Frame(instructions)
left_page.configure(background="white")
left_page.grid_propagate(False)
left_page.grid(row=0, column=0, sticky="nsew")

left_page.grid_columnconfigure(0, weight=1)
left_page.grid_rowconfigure(0, weight=1)
left_page.grid_rowconfigure(1, weight=1)
left_page.grid_rowconfigure(2, weight=1)
left_page.grid_rowconfigure(3, weight=3)
left_page.grid_rowconfigure(4, weight=1)
left_page.grid_rowconfigure(5, weight=1)

left_page_text1 = tk.Label(left_page, text="HOW TO PLAY", font=("Verdana", 22, "bold underline"), anchor="n")
left_page_text1.configure(background="white")
left_page_text1.grid(row=0, column=0, sticky="n")

left_page_text2 = tk.Label(left_page, text="At the start of each game, the user player will have the ability to choose either X’s or O’s.", font=("Verdana", 16), wraplength=550, justify="left")
left_page_text2.configure(background="white")
left_page_text2.grid(row=1, column=0, sticky="w")

left_page_text3 = tk.Label(left_page, text="The objective for this game is to be the first person to get 3 of their shape (X’s or O’s) in a row. If neither player successfully gets 3 of their shape in a row, and the board is filled up, the result is a tie. At the end of the game, you will be presented with the ability to play again.", font=("Verdana", 15), wraplength=550, justify="left") 
left_page_text3.configure(background="white")
left_page_text3.grid(row=2, column=0, sticky="w")

left_page_text4 = tk.Label(left_page, text="OPPONENT", font=("Verdana", 22, "bold underline"), anchor="n")
left_page_text4.configure(background="white")
left_page_text4.grid(row=4, column=0, sticky="n")

left_page_text5= tk.Label(left_page, text="In this game, you will be playing against a computer-player that will use the shape opposite to the user. This computer will randomly make moves throughout the game. Each game will have unique moves selected by the computer. ", font=("Verdana", 15), wraplength = 550, justify="left")
left_page_text5.configure(background="white")
left_page_text5.grid(row=5, column=0, sticky="w")

right_page =tk.Frame(instructions)
right_page.configure(background="white")
right_page.grid_propagate(False)
right_page.grid(row=0, column=2, sticky="nsew")

right_page.grid_columnconfigure(0, weight=1)
right_page.grid_rowconfigure(0, weight=1)
right_page.grid_rowconfigure(1, weight=1)
right_page.grid_rowconfigure(2, weight=2)
right_page.grid_rowconfigure(3, weight=1)
right_page.grid_rowconfigure(4, weight=1)

right_page_text1 = tk.Label(right_page, text="About the Creator:", font=("Verdana", 22, "bold underline"), anchor="n")
right_page_text1.configure(background="white")
right_page_text1.grid(row=0, column=0, sticky="n")

right_page_text2= tk.Label(right_page, text="This version of Tic-Tac-Toe was recreated by Purab Natalia. It was created using Python’s Tkinter GUI module and Python’s random module. Purab Natalia worked on this project during January of 2025. He was a freshman at Penn State studying Computer Science when he began this project.", font=("Verdana", 15), wraplength=550, justify="left")
right_page_text2.configure(background="white")
right_page_text2.grid(row=1, column=0, sticky="w")

right_page_text3= tk.Label(right_page, text="Final Words/Thoughts:", font=("Verdana", 22, "bold underline"), wraplength=550, anchor="n")
right_page_text3.configure(background="white")
right_page_text3.grid(row=3, column=0, sticky="n")

right_page_text4= tk.Label(right_page, text="As you go through the experience, make sure to remember to have fun! Thank you for checking out the project!", font=("Verdana", 15), wraplength=550, justify="left")
right_page_text4.configure(background="white")
right_page_text4.grid(row=4, column=0, sticky="w")



#### GAMEPAGE GUI
player_shape = None
computer_shape = None
current_user_turn = None

game_board = ["", "", "", "", "", "", "", "", ""]

game_page = tk.Frame(root)
game_page.configure(background="black")
game_page.grid(row=0, column=0, sticky="nsew")

game_page.grid_rowconfigure(1, weight=1)
game_page.grid_rowconfigure(2, weight=2)
game_page.grid_rowconfigure(3, weight=2)
game_page.grid_rowconfigure(4, weight=20)
game_page.grid_rowconfigure(5, weight=20)
game_page.grid_rowconfigure(6, weight= 40)
game_page.grid_rowconfigure(7, weight=2)

game_page.grid_columnconfigure(1, weight=1)

help_btn2 = tk.Button(game_page, text="Help", command=lambda:help("game_page"))
help_btn2.grid(row=2, column=1)
help_btn2.configure(width=16, height=3, font=("Verdana", 12, "bold"))

return_home_button = tk.Button(game_page, text="Return Home", command=return_home)
return_home_button.grid(row=3, column=1)
return_home_button.configure(width=16, height=4, font=("Verdana", 12, "bold"))


board = tk.Canvas(game_page)
board.configure(width=420, height=420)
board.grid(row=5, column=1)
board.create_line(140, 0, 140, 420)
board.create_line(280,0,280,420)
board.create_line(0, 140, 420, 140)
board.create_line(0, 280, 420, 280)

board.bind("<Button-1>", board_click)


shape_selection = tk.Frame(game_page)
shape_selection.grid(row=4, column=1)
shape_selection.configure(background="black")

shape_question = tk.Label(shape_selection, text="Please pick a shape: Either X's or O's.")
shape_question.grid(row=3, column=1)
shape_question.configure(background="dark blue", foreground="white", font=("Verdana", 12, "bold"))

x_button = tk.Button(shape_selection, text="X", command=lambda: choose_shape("X"))
o_button = tk.Button(shape_selection, text="O", command=lambda: choose_shape("O"))

x_button.grid(row=5, column=0, padx=10, pady=10)
o_button.grid(row=5, column=2, padx=10, pady=10)


game_status = tk.Label(game_page, text="")
game_status.grid(row=4, column=1)
game_status.configure(background="black", foreground="white", font=("Verdana", 16, "bold"))

game_status.lower(shape_selection)


play_again_button = tk.Button(game_page, text="Play Again", command=play_again)
play_again_button.grid(row=6, column=1)
play_again_button.configure(width=16, height=3, font=("Verdana", 12, "bold"))
play_again_button.grid_remove()



###UPON LAUNCH
show_frame(welcome_page)
root.mainloop()