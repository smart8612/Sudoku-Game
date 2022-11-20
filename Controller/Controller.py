from Model.SudokuGame import SudokuGame


class Controller:
    game = SudokuGame()

    def get_pane(self) -> list:
        return self.game.pane

    def set_pane(self, pane):
        self.game.pane = pane

    def get_max_size(self) -> int:
        return self.game.MAX_SIZE

    def reset(self):
        self.game = SudokuGame()

    def solve(self) -> bool:
        return self.game.solve()
