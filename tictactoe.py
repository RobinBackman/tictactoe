import numpy as np
import os
import time


# Display the board
def display_board():
    # 0 represents an empty slot
    # 1 is Player one (X)
    # 2 is Player two (O)
    internal_board = []

    for slot in board.flatten():
        if slot == 0:
            internal_board.append(' ')
        elif slot == 1:
            internal_board.append('X')
        elif slot == 2:
            internal_board.append('O')

    print("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}
    """.format(*internal_board))

# Let player one or two choose a spot
def choose_spot(spot, player):
    if spot.isdigit():
        index = np.where(selection_board == int(spot))

        if board[index] == 0:
            board[index] = player
        else:
            selected_spot = input(f"The spot was taken, select a new one (1-9) >> ")
            choose_spot(selected_spot, current_player)
    else:
        selected_spot = input(f"Not a valid character, try again! (1-9) >> ")
        choose_spot(selected_spot, current_player)

def check_win(last_player):
    mask = board == last_player
    out = mask.all(0).any() | mask.all(1).any() # Check axis 0 (Rows) and axis 1 (cols)
    out |= np.diag(mask).all() | np.diag(mask[:, ::-1]).all() # Check the diagonals

    return out

def check_draw():
    mask = board == 0

    return not mask.any() # Returns true if its a draw 


# The gameboard
board = np.zeros((3, 3), np.int8)

# This board represents all the choices,
# makes it easy to look if spot is available with numpy
selection_board = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

current_player = 1

if __name__ == '__main__':
    print("TICTACTOE - BY ROBIN BACKMAN")
    time.sleep(2)

    playing = True
    while playing:
        os.system("clear")
        display_board()
        selected_spot = input(f"Player {current_player}, select a spot(1-9) >> ")
        choose_spot(selected_spot, current_player)

        is_winner = check_win(current_player)
        is_draw = check_draw()

        if is_winner or is_draw:
            playing = False
            os.system("clear")
            display_board()

            if is_winner:
                print(f'Player {current_player} wins the game!')
            elif is_draw:
                print(f'It was a draw!')

        if current_player == 1:
            current_player = 2
        elif current_player == 2:
            current_player = 1
