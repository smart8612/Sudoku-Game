import unittest
from Model.SudokuGame import SudokuGame


class MyTestCase(unittest.TestCase):
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

    def setUp(self) -> None:
        self.game = SudokuGame()

    def tearDown(self) -> None:
        del self.game

    def test_4by4_enter_same_return(self):
        for pane in self.testCase:
            self.game.write(pane)

            for row in range(0, 4):
                for col in range(0, 4):
                    game_pane_value = self.game.pane[row][col]
                    test_pane_value = pane[row][col]
                    self.assertEqual(game_pane_value, test_pane_value)

    def test_입력된_수도쿠_판이_완성될_수_있는지_검증_한다(self):
        for pane in self.testCase:
            self.game.write(pane)
            is_success = self.game.solve()
            self.assertTrue(is_success)


if __name__ == '__main__':
    unittest.main()
