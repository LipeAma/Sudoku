class Game():
    def __init__(self, starting_string) -> None:
        self.start = starting_string
        self.board = starting_string
        self.undo = []

    def get_starting_conditions(self):
        return self.start
    
    def get_board(self, array_like = False):
        if array_like:
            array = []
            for n in range(9):
                array.append([])
                for char in self.board[n*9:9*(n+1)]:
                    array[n].append(int(char))
            return array 
        else: return self.board
    
    def __str__(self) -> str:
        return self.board
    
    def update(self, line, row, value):
        self.undo.append((line, row, self.string[line*9+row]))
        self.string[line*9+row] = str(value)
    
    def reset_game(self):
        self.board = self.start
    
    def undo(self):
        index = len(self.undo) - 1
        line, row, value = self.undo.pop[index]
        self.update(line, row, value)
    

if __name__ == '__main__':
    strin = '070000043040009610800634900094052000358460020000800530080070091902100005007040802'
    my_game = Game(strin)
    print(my_game.get_board(True))