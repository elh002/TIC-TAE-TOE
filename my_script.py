import sys

sys.path.append('../')

import my_module.functions as fn


if __name__ == '__main__':
    game = fn.start_game()
    fn.display_game(game)
    player = 1
    winner = 0  # the winner is not yet defined

# while loop

"""
     This while loop is to limit playersin range 1-3, anything above 3 is false and it will go back so          the player
    have to put correct input in order to process the game
    
"""
    while winner == 0 and fn.moves_exist(game):
        print("Currently player: " + str(player))
        available = False
        while not available:#check input if it is above 4.
            row = fn.convert_input_to_coordinate(int(input("Which row? (start with 1-3) ")))
            while row < 0 or row > 2:
                row = fn.convert_input_to_coordinate(int(input("Wrong input? (start with 1-3) ")))
"""
    This while loop is to limit playersin range 1-3 column, row so each player has to pick a square in 
    row and column.
    
"""          
            column = fn.convert_input_to_coordinate(int(input("Which column? (start with 1-3) ")))
            while column < 0 or column > 2:
                column = fn.convert_input_to_coordinate(int(input("Wrong input? (start with 1-3) ")))
"""
    When player 1 or player 2 places three respective marks (X or O) “OOO” or “XXX”
    horizontally, vertically or diagonally will be the winner. the output would be "Player 1 or 2  Wins!"

"""

            available=fn.check_empty_space(game, row, column)
            print(fn.check_empty_space(game, row, column))
            if fn.check_empty_space(game, row, column):
                game = fn.add_piece(game, player, row, column) 
        if fn.check_winner(game):
            break
        fn.display_game(game)
        player = fn.switch_player(player)
        winner = fn.check_winner(game)
    fn.display_winner(winner)


