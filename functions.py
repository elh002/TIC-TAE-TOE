# Draw the line to make the box 
def draw_line(width, edge, fill):
    print(fill.join([edge] * (width + 1)))

'''
print who is the winner in player 1 and 2
'''
def display_winner(player):
    if player == 0:
        print("Game Over! No winner!")
        return False
    else:
        print("Player " + str(player) + " Wins!")
        return True

def check_row_winner(row):
    '''
    input: row - list
    
    checks to see if all elements in the list are the same
    
    Return to the play number if the player 1 or 2 wins for that row.
    However, no player wins, it return to 0 and restart the game!
    '''

    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    return 0

#("which row?")
    '''
    define the column from 1-3
    '''
def put_col(game, col_number):
    return [game[X][col_number] for X in range(3)]
'''
define the row from 1-3
'''

def put_row(game, row_number):
    return game[row_number]
'''
define check row to check if row is in range 1-3
'''
def check_row(lst):
    for i in range(3):
        if lst[i][0] == lst[i][1] and lst[i][1] == lst[i][2]:
            return lst[i][0]
    return 0
'''define check_diagnal to make sure the diagnal in range from 1-3'''
def check_diagnal(lst):
    if lst[0][0] == lst[1][1] and lst[1][1]== lst[2][2]:
        return lst[0][0]
    elif lst[0][2] == lst[1][1] and lst[2][0] == lst[1][1]:
        return lst[0][2]
    else:
        return 0
    
 '''
 check_vertical to make sure the vertical in range from 1-3,  it places 3 respective marks (X or O)
'''    
    
def check_vertical(lst):
    for i in range(3):
        if lst[0][i] == lst[1][i] and lst[1][i] == lst[2][i]:
            return lst[0][i]
    return 0
    
'''
 check_winner to make sure the vertical in range from 1-3,  it places 3 respective marks (X or O)
'''  
def check_winner(game):
    if check_row(game) != 0:
        return check_row(game)
    elif check_diagnal(game) != 0:
        return  check_diagnal(game)
    elif check_vertical(game) !=0:
        return  check_vertical(game)
    else:
        return 0
'''
 start_game is for player to place mark in range 1-3 diagnal, horizontal, vertical in range from 1-3,  it places 3 respective marks (X or O)
'''   

def start_game():
    return [[0, 0, 0] for O in range(3)]
'''
 display_game is for player 1 and 2 to place mark in range 1-3 diagnal, 
 horizontal, vertical in range from 1-3,  it places 3 respective marks (X or O)
'''   
def display_game(game):
    d = {2: "X", 1: "O", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")
"""
add_piece is for player 1 and 2 to place mark O or X in the box from range 1-3 row and column diagnal, 
 horizontal, vertical in range from 1-3,  it places 3 respective marks (X or O)
"""


def add_piece(game, player, row, column):
    game[row][column] = player
    return game

"""
check_empty_space is for any of the players have picked a square/box then the other player cannot override that
"""

def check_empty_space(game, row, column):
    return game[row][column] == 0

"""
convert_input_to_coordinate is for any of the players had picked a square/box then keep track 
on if they are getting triple "OOO" or "XXX" the other player cannot override that
"""


def convert_input_to_coordinate(user_input):
    return user_input - 1


"""
switch_player is switching form player 1 to player 2 and player 1 again and so on.
"""

def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1
    
"""
moves_exist is for switching cloumn and row for player to pick a square.
"""


def moves_exist(game):
    for row_num in range(3):
        for col_num in range(3):
            if game[row_num][col_num] == 0:
                return True
    return False

