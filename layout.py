import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFrame, QHBoxLayout
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.labels = []

        self.v_layout = QVBoxLayout(self)

        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(10,40,0,0)

        self.central_widget = QWidget()
        self.central_widget.setMaximumWidth(200)

        self.button = QPushButton('click', self.central_widget)
        self.button.clicked.connect(self.add_card)

        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(600,600)

    def add_card(self):
        self.second_class = custom_widget()
        label = self.second_class
        self.labels.append(label)
        layout = self.v_layout
        layout.addWidget(label.frame)


class custom_widget:
    def __init__(self):
        super().__init__()

        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: #f0f0f0; border: 2px solid black; border-radius: 10px;")
        self.vertical_layout = QVBoxLayout()
        self.horizontal_one = QHBoxLayout()
        self.horizontal_two = QHBoxLayout()

        self.vertical_layout.addLayout(self.horizontal_one)
        self.vertical_layout.addLayout(self.horizontal_two)

        self.label = QLabel('Your task')
        self.horizontal_one.addWidget(self.label)

        self.button_done = QPushButton('Done')
        self.button_done.setFixedSize(50,25)
        self.button_done.setStyleSheet("background-color: green; border: 2px solid black; border-radius: 10px;")
        self.button_done.clicked.connect(lambda: print('done'))
        self.horizontal_one.addWidget(self.button_done)

        self.label_date = QLabel('Creation date: ')
        self.horizontal_two.addWidget(self.label_date)

        self.button_delete = QPushButton('Delete')
        self.button_delete.setFixedSize(50,25)
        self.button_delete.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 10px;")
        self.button_delete.clicked.connect(lambda : print('deleted'))
        self.horizontal_two.addWidget(self.button_delete)

        self.frame.setLayout(self.vertical_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
