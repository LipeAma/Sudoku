import numpy as np
import pandas as pd
import random

def quadrant_to_line(matrix):
    result = []
    for m in [0,3,6]:
        for n in [0,3,6]: result.append(matrix[m:m+3,n:n+3].reshape(9))
    return np.array(result)

def does_not_repet_in_line(matrix):
    result = np.ones((9,9), np.int8)
    for m in range(9):
        for n1 in range(9):
            for n2 in range(n1+1, 9):
                if matrix[m][n1] == matrix[m][n2]: result[m][n1] = result[m][n2] = 0
    return result

def string_to_array(string):
    array = np.zeros((9,9), np.int8)
    for m in range(9): 
        for n in range(9): array[m][n] = string[m*9+n]
    return array

def array_to_string(array):
    string = ''
    for line in array:
        for number in line: string += str(number)
    return string


class Game():
    def __init__(self, string = None):
        self.undo = []
        self.wrong = np.zeros((9,9), np.int8)
        if string is None : self.string = Game.random_string()
        else: self.string = string
        self.board = string_to_array(self.string)
        self.is_blocked = np.zeros((9,9), np.int8)
        for k, j in np.transpose(self.board.nonzero()):
            self.is_blocked[k][j] = 1

    @staticmethod
    def random_string():
        a = random.randrange(0,10)
        b = random.randrange(0,10000)
        file = pd.read_csv(f'database/{a}.csv')
        string = file['puzzle'].get(b)
        del file
        return str(string)

    def get_board(self):
        return(self.board)
    
    def get_blocked(self):
        return(self.is_blocked)

    def update_game(self, value, position):
        m, n = position
        if value != self.board[m][n] and not self.is_blocked[m][n]:
            self.undo.insert(0, (self.board[m][n], m, n))
            self.board[m][n] = value
    
    def get_correct(self):
        correct_in_quadrant = quadrant_to_line(does_not_repet_in_line(quadrant_to_line(self.board)))
        correct_in_line = does_not_repet_in_line(self.board)
        correct_in_column = does_not_repet_in_line(self.board.transpose()).transpose()
        self.correct = correct_in_quadrant * correct_in_line * correct_in_column
        return self.correct
    
    def check_victory(self):
        board_string = array_to_string(self.board)
        correct_string = array_to_string(self.get_correct())
        if board_string.count('0') == 0 and correct_string.count('0') == 0: return True
        else: return False

