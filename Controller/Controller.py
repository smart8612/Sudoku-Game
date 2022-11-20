from Model.SudokuGame import SudokuGame


class Controller:
    game = SudokuGame()

    def __init__(self):
        print("Hello World")

    def get_pane(self) -> list:
        return self.game.pane

    def set_pane(self, pane):
        self.game.pane = pane

    def reset(self):
        self.game = SudokuGame()

    def solve(self) -> bool:
        return self.game.solve()
