import copy

class SudokuGame:
    pane = [[]]

    def __init__(self):
        print("Init sudoku game")

    def run(self):
        print("Run sudoku game")

    def write(self, pane):
        self.pane = copy.deepcopy(pane)

    def solve(self):
        print("solve")

SudokuGame()