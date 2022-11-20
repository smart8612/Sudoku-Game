from PyQt6.QtWidgets import QApplication
from View.MainWindow import MainWindow
import sys


class AppDelegate:
    app = QApplication(sys.argv)
    window = MainWindow()

    __window_title = "Sudoku Game Solver"

    def __init__(self):
        self.__configure()

    def run(self):
        self.app.exec()

    def __configure(self):
        self.window.show()
        self.window.setWindowTitle(self.__window_title)
