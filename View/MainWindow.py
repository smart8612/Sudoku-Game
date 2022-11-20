from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 500))
        self.button = QPushButton("Push for Window")
        self.setCentralWidget(self.button)