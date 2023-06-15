import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFrame, QHBoxLayout)
from PyQt5.QtCore import Qt
from card import MyWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.frm1 = QFrame(self)
        self.frm2 = QFrame(self)
        self.frm3 = QFrame(self)

        self.labels = []

        self.h_layout = QHBoxLayout(self)

        self.v_layout = QVBoxLayout(self.frm1)
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0,40,0,0)
        # self.central_widget = QWidget()
        # self.central_widget.setMaximumWidth(200)

        # self.central_widget.setLayout(self.v_layout)
        # self.h_layout.addWidget(self.central_widget)
        self.h_layout.addWidget(self.frm1)

        # self.button = QPushButton('click', self.central_widget)
        self.button = QPushButton('click')

        # self.button.clicked.connect(self.add_card)
        self.button.clicked.connect(self.card_add_card)

        self.v_layout2 = QVBoxLayout(self.frm2)
        self.v_layout2.setAlignment(Qt.AlignTop)
        self.v_layout2.setContentsMargins(0,40,0,0)
        # self.central_widget2 = QWidget()
        # self.central_widget2.setMaximumWidth(200)

        # self.label_test = QLabel('POPS')
        # self.v_layout2.addWidget(self.label_test)

        # self.central_widget2.setLayout(self.v_layout2)
        self.h_layout.addWidget(self.frm2)

        self.v_layout3 = QVBoxLayout(self.frm3)
        self.v_layout3.setAlignment(Qt.AlignTop)
        self.v_layout3.setContentsMargins(0,40,0,0)

        # self.central_widget3 = QWidget()
        # self.central_widget3.setLayout(self.v_layout3)
        self.h_layout.addWidget(self.frm3)
        # self.label_3 = QLabel('textAAAAAAAAAAAA')
        # self.v_layout3.addWidget(self.label_3)

        self.main_layout = QWidget()
        self.main_layout.setLayout(self.h_layout)
        self.setCentralWidget(self.main_layout)
        self.setMinimumSize(600,600)

        self.v_layout3.addWidget(self.button)

        self.temp_frame = QFrame()
        self.temp_frame.setStyleSheet("background-color: yellow; border: 2px solid black; border-radius: 10px;")

    def add_card(self):
        self.second_class = custom_widget()
        label = self.second_class
        self.labels.append(label)
        layout = self.v_layout
        layout.addWidget(label.frame)

    def card_add_card(self):
        self.second_class = custom_widget()
        label = self.second_class
        self.labels.append(label)
        layout = self.v_layout
        layout.addWidget(label.frame)

    def card_to_move(self):
        layout = self.v_layout2
        layout.addWidget(self.temp_frame)


class custom_widget:
    def __init__(self):
        super().__init__()

        obj = MyWindow()

        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: #f0f0f0; border: 2px solid black; border-radius: 10px;")
        self.vertical_layout = QVBoxLayout()
        self.horizontal_one = QHBoxLayout()
        self.horizontal_two = QHBoxLayout()

        self.vertical_layout.addLayout(self.horizontal_one)
        self.vertical_layout.addLayout(self.horizontal_two)

        self.label = QLabel('Your task')
        self.horizontal_one.addWidget(self.label)

        self.button_done = QPushButton('Move')
        self.button_done.setFixedSize(50,25)
        self.button_done.setStyleSheet("background-color: green; border: 2px solid black; border-radius: 10px;")
        self.horizontal_one.addWidget(self.button_done)
        # self.button_done.clicked.connect(lambda : print('moved'))
        self.button_done.clicked.connect(lambda : obj.card_to_move(self))

        self.label_date = QLabel('Creation date: ')
        self.horizontal_two.addWidget(self.label_date)

        self.button_delete = QPushButton('Delete')
        self.button_delete.setFixedSize(50,25)
        self.button_delete.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 10px;")
        self.button_delete.clicked.connect(self.delete_card)
        self.horizontal_two.addWidget(self.button_delete)

        self.frame.setLayout(self.vertical_layout)

    def delete_card(self):
        self.frame.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
