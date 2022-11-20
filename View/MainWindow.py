from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtWidgets import QPushButton, QLineEdit
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 450))
        self.__configure_layout()

    def __configure_layout(self):
        self.layout = QVBoxLayout()

        self.__configure_title_label()
        self.layout.addWidget(self.title_label)

        self.__configure_sudoku_pane()
        self.layout.addLayout(self.game_pane_layout)

        self.__configure_status_label()
        self.layout.addWidget(self.status_label)

        self.__configure_control_buttons()
        self.layout.addLayout(self.control_buttons_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def __configure_title_label(self):
        self.title_label = QLabel("[ Sudoku Game ]")

    def __configure_status_label(self):
        self.status_label = QLabel("Sudoku Game Status Label")

    def __configure_sudoku_pane(self):
        self.game_pane_layout = QGridLayout()
        max_size = 4
        inputs = [[QLineEdit() for _ in range(max_size)] for _ in range(max_size)]
        for row in range(max_size):
            for col in range(max_size):
                self.game_pane_layout.addWidget(inputs[row][col], row, col)

    def __configure_control_buttons(self):
        self.control_buttons_layout = QHBoxLayout()

        buttons = [QPushButton("Start"), QPushButton("Reset")]
        for button in buttons:
            self.control_buttons_layout.addWidget(button)
            button.clicked.connect(self.__button_clicked)

    def __button_clicked(self):
        print("Button was clicked")
