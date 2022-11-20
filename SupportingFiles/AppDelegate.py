from PyQt6.QtWidgets import QApplication, QWidget
import sys


class AppDelegate:
    app = QApplication(sys.argv)
    window = QWidget()

    def __init__(self):
        self.__configure()

    def run(self):
        self.app.exec()

    def __configure(self):
        self.window.show()
