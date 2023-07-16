import numpy as np

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

class Game():
    def __init__(self, game_string):
        self.undo = []
        self.wrong = np.zeros((9,9), np.int8)
        self.game_string = game_string
        self.board = np.zeros((9,9), np.int8)
        for m in range(9): 
            for n in range(9): self.board[m][n] = game_string[m*9+n]
        self.is_blocked = np.zeros((9,9), np.int8)
        for k, j in np.transpose(self.board.nonzero()):
            self.is_blocked[k][j] = 1

    def get_board(self):
        return(self.board)
    
    def get_blocked(self):
        return(self.is_blocked)

    def update_game(self, pressed_key, position):
        new_char, mod = pressed_key
        m, n = position
        if new_char != self.board[m][n] and not self.is_blocked[m][n]:
            self.undo.insert(0, (self.board[m][n], m, n))
            self.board[m][n] = new_char
    
    def get_correct(self):
        correct_in_quadrant = quadrant_to_line(does_not_repet_in_line(quadrant_to_line(self.board)))
        correct_in_line = does_not_repet_in_line(self.board)
        correct_in_column = does_not_repet_in_line(self.board.transpose()).transpose()
        correct = correct_in_quadrant * correct_in_line * correct_in_column
        return correct