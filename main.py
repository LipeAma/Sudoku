from sudoku_gui import run_game
from sudoku_resources import Game

"""print('\n\nType \'exit\' or \'play\'')
running_cli = True
while running_cli:
    user_input = input('sudoku: ')
    if user_input == 'play':
        print('The game has opened. Typing is prevented while the window is open')
        game = Game()
        run_game(game)
        print('Game closed.')
    elif user_input == 'exit':
        print('Bye')
        running_cli = False
    else: print('type \'exit\' or \'play\'')
"""

game = Game()
run_game(game)