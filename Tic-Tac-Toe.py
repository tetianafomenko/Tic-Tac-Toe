# Create the board 
board = {
    "A": ["-","-","-"],
    "B": ["-","-","-"],
    "C": ["-","-","-"]}

# Show the board in terminal
def display_board(board):
    print("~~~~~~~~~~~~~~~~~~~~")
    print("       BOARD")
    for cell in board:
        print( cell, board[cell])
    print("    0    1    2")
    print("~~~~~~~~~~~~~~~~~~~~")

# Assign names and marks to each player
Player_1 = {'name': '', 'mark': 'O', 'winner': False}
Player_2 = {'name': '', 'mark': 'X', 'winner': False}

def reset_values():
    Player_1 = {'name': '', 'mark': 'O', 'winner': False}
    Player_2 = {'name': '', 'mark': 'X', 'winner': False}
    board = {
    "A": ["-","-","-"],
    "B": ["-","-","-"],
    "C": ["-","-","-"]}

# Get the names and communicate the marks
def intro():
    print("Player 1, what is your name?")
    Player_1["name"] = input()
    Player_1["mark"] = str(Player_1['name'][0])
    print("Get ready to throw down, " + Player_1["name"] + "! You will play with " + Player_1["mark"] + "!")
    print("Player 2, what is your name?")
    Player_2["name"] = input()
    Player_2["mark"] = str(Player_2['name'][0])
    print("Get ready to throw down, " + Player_2["name"] + "! You will play with " + Player_2["mark"] + "!")
    active_player = Player_1
    return active_player

def announce_winner(playa):
    print("Congratulations, " + playa['name'] + ", you have won!!!")
    display_board(board)
    return playa
    
def check_win(symbol, active_player, turn):
    if board["A"][0] == active_player['mark'] and board["A"][1] == active_player['mark'] and board["A"][2] == active_player['mark']:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["B"][0] == symbol and board["B"][1] == symbol and board["B"][2] == symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["C"][0] == symbol and board["C"][1] == symbol and board["C"][2] == symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["A"][0] == symbol and board["B"][0] == symbol and board["C"][0] == symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["A"][1] == symbol and board["B"][1] == symbol and board["C"][1] == symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["A"][2] == symbol and board["B"][2] == symbol and board["C"][2] == symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["A"][0]==symbol and board["B"][1]== symbol and board["C"][2]==symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    elif board["A"][2]==symbol and board["B"][1]== symbol and board["C"][0]==symbol:
        active_player['winner'] = True
        return announce_winner(active_player)
        reset_values()
    else:
        if turn == 9:
            print("There has been a Tie. Do you want to play again? Y/N")
            answer = input()
            if answer == "Y" or answer == "y":
                game()
            elif answer == "N" or answer == "n":
                print("Farewell!")

# Offer a turn to each player
def take_turns(active_player=Player_1):
    for turn in range(10):
        if Player_1['winner'] == True or Player_2['winner'] == True:
            print("Do you want to play again? Y/N")
            answer = input()
            if answer == "Y" or answer == "y":
                game()
            elif answer == "N" or answer == "n":
                print("Farewell!")
        else:
            display_board(board)
            print('Turn for ' + active_player["name"] + '. Move on which space?')
            the_move = input()
            insert(the_move, active_player, turn)
            # check_win(the_move, active_player, turn)
            turn += 1
            if active_player == Player_1:
                active_player = Player_2
            else:
                active_player = Player_1

# Update the table with entered coordinates
def insert(coord, active_player, turn):
    try:
      x, y = coord[0].upper(), int(coord[1])
      if active_player == Player_1:
        if board[x][y] == Player_1['mark'] or board[x][y] == Player_2['mark']:
            print("That space is already occupied, try a new space!")
            new_coord = input()
            insert(new_coord, active_player, turn)
        else:
            board[x][y] = Player_1["mark"]
            check_win(Player_1["mark"], Player_1, turn)
      elif active_player == Player_2:
        if board[x][y] == Player_1['mark'] or board[x][y] == Player_2["mark"]:
            print('That space is already occupied, try a new space!')
            new_coord = input()
            insert(new_coord, active_player, turn)
        else:
          board[x][y] = Player_2["mark"]
          check_win(Player_2["mark"], Player_2, turn)
    except ValueError: #if input is a special character 
        print("That was an invalid value. Wanna try again?")
        new_coord = input()
        insert(new_coord, active_player, turn)
    except IndexError: #if input is out of range
        print("That was an invalid entry. Wanna try again?")
        new_coord = input()
        insert(new_coord, active_player, turn)
    except:
        print("That was a weird entry, wanna try that again?")
        new_coord = input()
        insert(new_coord, active_player, turn)
    return coord, active_player, turn

# Make the layout of the game
def game():
    intro()
    take_turns()

# Play game
game()