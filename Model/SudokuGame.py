import copy


class SudokuGame:
    pane = []

    MAX_SIZE = 4
    MAX_BOX_SIZE = 2
    UNASSIGNED = 0

    def __init__(self):
        self.pane = [
            [self.UNASSIGNED]*self.MAX_SIZE for _ in range(self.MAX_SIZE)
        ]

    def write(self, pane) -> None:
        self.pane = copy.deepcopy(pane)

    def solve(self) -> bool:
        row, col = self.__find_unassigned_position()
        if row == -1 and col == -1:
            return True

        for number in range(1, self.MAX_SIZE+1):
            if self.__is_promising(row, col, number):
                self.pane[row][col] = number
                if self.solve():
                    return True
                self.pane[row][col] = self.UNASSIGNED

        return False

    def __find_unassigned_position(self) -> (int, int):
        for row in range(self.MAX_SIZE):
            for col in range(self.MAX_SIZE):
                if self.pane[row][col] == self.UNASSIGNED:
                    return row, col
        return -1, -1

    def __is_promising(self, row, col, number) -> bool:
        is_not_used_on_row_and_col = not self.__is_used_in_row(row, number) and not self.__is_used_in_col(col, number)
        is_not_used_on_box = not self.__is_used_in_box(row, col, number)
        is_unassigned = self.pane[row][col] == self.UNASSIGNED
        return is_not_used_on_row_and_col and is_not_used_on_box and is_unassigned

    def __is_used_in_row(self, row, number) -> bool:
        for col in range(self.MAX_SIZE):
            if self.pane[row][col] == number:
                return True
        return False

    def __is_used_in_col(self, col, number) -> bool:
        for row in range(self.MAX_SIZE):
            if self.pane[row][col] == number:
                return True
        return False

    def __is_used_in_box(self, row, col, number) -> bool:
        box_start_row = row - row % self.MAX_BOX_SIZE
        box_start_col = col - col % self.MAX_BOX_SIZE

        for r in range(self.MAX_BOX_SIZE):
            for c in range(self.MAX_BOX_SIZE):
                marking_value = self.pane[r+box_start_row][c+box_start_col]
                if marking_value == number:
                    return True
        return False
