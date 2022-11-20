from Model.SudokuGame import SudokuGame


class Controller:
    game = SudokuGame()

    def __init__(self):
        print("Hello World")

    def get_pane(self) -> list:
        return self.game.pane

    def reset(self):
        self.game = SudokuGame()
