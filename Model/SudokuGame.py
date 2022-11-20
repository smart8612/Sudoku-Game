import copy


class SudokuGame:
    pane = []

    def __init__(self):
        print("Init sudoku game")

    def run(self):
        print("Run sudoku game")

    def write(self, pane) -> None:
        self.pane = copy.deepcopy(pane)

    def solve(self) -> bool:
        print("solve")
        return True
