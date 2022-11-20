import unittest
from Model.SudokuGame import SudokuGame


class MyTestCase(unittest.TestCase):
    game = SudokuGame()

    testCase = [
                [[1, 2, 0, 0],
                 [0, 0, 1, 2],
                 [2, 1, 0, 0],
                 [4, 3, 0, 0]],
                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]],
                [[4, 0, 0, 0],
                 [0, 3, 0, 0],
                 [0, 0, 2, 0],
                 [0, 0, 0, 1]]
    ]

    def test_4by4_수도쿠_판이_입력_되면_동일한_판을_반환_해야_한다(self):
        for pane in self.testCase:
            self.game.write(pane)

            for row in range(0, 4):
                for col in range(0, 4):
                    game_pane_value = self.game.pane[row][col]
                    test_pane_value = pane[row][col]
                    if game_pane_value != test_pane_value:
                        self.assertFalse()
        self.assertTrue()


if __name__ == '__main__':
    unittest.main()
