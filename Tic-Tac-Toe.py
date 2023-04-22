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
   if turn_count / 2 == 0:
        return player_1_name
   else:
        return player_2_name

# Offer a turn to each player
def turn():
    global turn_count
    active_player = check_active_player()
    if active_player == player_1_name:
        print(player_1_name + ", it's your turn! Which cell do you want to mark as yours?")
        print(board)
        marked_cell = input()
    elif active_player == player_2_name:
        print(player_2_name + ", it's your turn! Which cell do you want to mark as yours?")
        print(board)
        marked_cell = input()
    else:
        print("Error")
    turn_count += 1

turn()

# if turn_count >= 5:
