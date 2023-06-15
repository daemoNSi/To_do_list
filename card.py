import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFrame, QHBoxLayout)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout(self)

        self.frm1 = QFrame(self)
        self.frm1.setStyleSheet("background-color: blue; border: 2px solid black; border-radius: 10px;")

        self.layout_in_h1 = QVBoxLayout(self.frm1)
        self.horizontal_one = QHBoxLayout()
        self.horizontal_two = QHBoxLayout()
        self.layout_in_h1.addLayout(self.horizontal_one)
        self.layout_in_h1.addLayout(self.horizontal_two)

        self.label = QLabel('Your task')
        self.horizontal_one.addWidget(self.label)

        self.button_done = QPushButton('Move')
        self.button_done.clicked.connect(self.on_click)
        self.button_done.setStyleSheet("background-color: green; border: 2px solid black; border-radius: 10px;")
        self.horizontal_one.addWidget(self.button_done)

        self.label_date = QLabel('Creation date: ')
        self.horizontal_two.addWidget(self.label_date)

        self.button_delete = QPushButton('Delete')
        self.button_delete.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 10px;")
        self.horizontal_two.addWidget(self.button_delete)

        self.layout_in_h2 = QVBoxLayout()

        self.h_layout.addWidget(self.frm1)

        self.frm2 = QFrame(self)
        self.frm2.setStyleSheet('background-color: purple')
        self.h_layout.addWidget(self.frm2)

        self.v_lay1 = QVBoxLayout(self.frm1)

        self.v_lay2 = QVBoxLayout(self.frm2)

        self.main_layout = QWidget()
        self.main_layout.setLayout(self.h_layout)
        self.setCentralWidget(self.main_layout)
        self.setMinimumSize(250, 250)

        self.temp_frame = QFrame()
        self.temp_frame.setStyleSheet("background-color: yellow; border: 2px solid black; border-radius: 10px;")

    def on_click(self):
        # self.v_lay2.addWidget(self.layout_in_h1)
        self.v_lay2.addWidget(self.temp_frame)
        self.layout_in_h1 = QVBoxLayout(self.temp_frame)
        self.horizontal_one = QHBoxLayout()
        self.horizontal_two = QHBoxLayout()
        self.layout_in_h1.addLayout(self.horizontal_one)
        self.layout_in_h1.addLayout(self.horizontal_two)

        self.btn = QPushButton('Delete')
        self.btn.setStyleSheet("background-color: black; border: 2px solid black; border-radius: 10px;")
        self.horizontal_two.addWidget(self.btn)



    def card_move2(self, frame):
        layout = self.v_layout2
        layout.addWidget(frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(226, 129)
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(10, 20, 131, 31))
#         font = QtGui.QFont()
#         font.setFamily("MS Shell Dlg 2")
#         font.setPointSize(10)
#         self.label.setFont(font)
#         self.label.setAutoFillBackground(False)
#         self.label.setIndent(5)
#         self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(150, 10, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(Form)
#         self.pushButton_2.setGeometry(QtCore.QRect(140, 100, 75, 23))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(10, 110, 81, 16))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label.setText(_translate("Form", "Task"))
#         self.pushButton.setText(_translate("Form", "Delete"))
#         self.pushButton_2.setText(_translate("Form", "Completed"))
#         self.label_2.setText(_translate("Form", "DateCreated:"))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
