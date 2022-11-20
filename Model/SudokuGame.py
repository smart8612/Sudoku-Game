import copy


class SudokuGame:
    pane = []

    MAX_SIZE = 4
    UNASSIGNED = 0

    def __init__(self):
        self.pane = [
            [0]*self.MAX_SIZE for _ in range(self.MAX_SIZE)
        ]

    def write(self, pane) -> None:
        self.pane = copy.deepcopy(pane)

    def solve(self) -> bool:
        print("solve")
        return True

    def __find_unassigned_position(self, row, col) -> bool:
        pass

    def __is_promising(self, row, col, number) -> bool:
        pass

    def __is_used_in_row(self, row, number) -> bool:
        pass

    def __is_used_in_col(self, col, number) -> bool:
        pass

    def __is_used_in_box(self, row, col, number) -> bool:
        pass


if __name__ == '__main__':
    game = SudokuGame()
