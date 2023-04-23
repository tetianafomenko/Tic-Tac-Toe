# X Create a turns tracker

# Create error handling if the input is not equal to o or O or x or X
# Create win condition
# After each turn, check for win condition
# Write what happens when a win/draw condition is met

turn_count = 1

# Create the board 
board = {
    "A": ["-","-","-"],
    "B": ["-","-","-"],
    "C": ["-","-","-"]}

# Show the board in terminal
def display_board():
    print("~~~~~~~~~~~~~~~~~~~~")
    print("       BOARD")
    for cell in board:
        print( cell, board[cell])
    print("    0    1    2")
    print("~~~~~~~~~~~~~~~~~~~~")

print("Player 1, what is your name?")
player_1_name = input()
print("Get ready to throw down," + player_1_name + "! You will play with O")

print("Player 2, what is your name?")
player_2_name = input()
print("It's about to get intense, " + player_2_name + "! You will play with X.")

# print(board)

def check_active_player():
   global turn_count
   if turn_count / 2 != 0:
        return player_1_name
   else:
        return player_2_name

# Offer a turn to each player
def turn():
    global turn_count
    active_player = check_active_player()
    if turn_count < 5:
        if active_player == player_1_name:
            print(player_1_name + ", it's your turn! Which cell do you want to mark as yours?")
            display_board()
            marked_cell = input()
            # return marked_cell_o
        elif active_player == player_2_name:
            print(player_2_name + ", it's your turn! Which cell do you want to mark as yours?")
            display_board()
            marked_cell = input()
            # return marked_cell_x
    elif turn_count >= 5:
        check_win()
    else:
        print("Error")
    turn_count += 1
    return marked_cell
    return active_player

def check_win(active_player):
    if board["A"][0]==marked_cell and board["A"][1]== marked_cell and board["A"][2]==marked_cell:
        winner(player_here)
    elif board["B"][0]==marked_cell and board["B"][1]== marked_cell and board["B"][2]==marked_cell:
        winner(player_here)
    elif board["C"][0]==marked_cell and board["C"][1]== marked_cell and board["C"][2]==marked_cell:
        winner(player_here)
    elif board["A"][0]==marked_cell and board["B"][0]== marked_cell and board["C"][0]==marked_cell:
        winner(player_here)
    elif board["A"][1]==marked_cell and board["B"][1]== marked_cell and board["C"][1]==marked_cell:
        winner(player_here)
    elif board["A"][2]==marked_cell and board["B"][2]== marked_cell and board["C"][2]==marked_cell:
        winner(player_here)
    elif board["A"][0]==marked_cell and board["B"][1]== marked_cell and board["C"][2]==marked_cell:
        winner(player_here)
    elif board["A"][2]==marked_cell and board["B"][1]== marked_cell and board["C"][0]==marked_cell:
        winner(player_here)
    else:
        display_board()
        print("There has been a Tie")

turn()
check_win()
