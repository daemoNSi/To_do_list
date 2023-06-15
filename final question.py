import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFrame, QHBoxLayout, QLineEdit, QSystemTrayIcon, QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import json
import os
from datetime import datetime, timedelta
import atexit
import sched, time
import asyncio

filename = 'labels.json'
finish_to_date_json = 'to date.json'

class MyWindow(QMainWindow):
    dictionary_of_cards = {}
    finish_to_date_dict = {}

    def __init__(self):
        super().__init__()
        self.labels = []

        self.on_off = 'Disabled'

        self.h_layout = QHBoxLayout(self)
        self.first_horizont_v1 = QHBoxLayout(self)
        self.first_horizont_v2 = QHBoxLayout(self)
        self.first_horizont = QHBoxLayout(self)
        self.main_horizont = QHBoxLayout(self)
        self.first_horizont.addLayout(self.first_horizont_v1)
        self.first_horizont.addLayout(self.first_horizont_v2)

        self.label_to_date = QLabel('Finish to this date: ')
        self.first_horizont_v2.addWidget(self.label_to_date)

        self.label_task = QLabel('Your task: ')
        self.first_horizont_v1.addWidget(self.label_task)

        self.main_horizont.addLayout(self.h_layout)
        self.main_horizont.addLayout(self.first_horizont)

        self.entry = QLineEdit(self)
        self.to_date = QLineEdit(self)

        self.frm1 = QFrame(self)
        self.frm1.setFixedSize(240,50000)
        self.frm1.setStyleSheet("background-color: #EAC7C7; border: 2px solid black; border-radius: 10px;")

        self.frm2 = QFrame(self)
        self.frm2.setFixedSize(240,50000)
        self.frm2.setStyleSheet("background-color: #A0C3D2; border: 2px solid black; border-radius: 10px;")

        self.frm3 = QFrame(self)
        self.frm3.setFixedSize(240,50000)
        self.frm3.setStyleSheet("background-color: #F7F5EB; border: 2px solid black; border-radius: 10px;")

        self.layout_in_h1 = QVBoxLayout(self.frm1)
        self.layout_in_h1.setAlignment(Qt.AlignTop)
        self.layout_in_h2 = QVBoxLayout(self.frm2)
        self.layout_in_h2.setAlignment(Qt.AlignTop)
        self.layout_in_h3 = QVBoxLayout(self.frm3)
        self.layout_in_h3.setAlignment(Qt.AlignTop)

        self.h_layout.addWidget(self.frm1)
        self.h_layout.addWidget(self.frm2)
        self.h_layout.addWidget(self.frm3)

        self.main_layout = QWidget()
        self.main_layout.setLayout(self.main_horizont)
        self.setCentralWidget(self.main_layout)

        self.btn_add_card = QPushButton('Add card')
        self.btn_add_card.clicked.connect(self.add_card)
        self.h_layout.addWidget(self.btn_add_card)
        self.first_horizont_v1.addWidget(self.entry)
        self.first_horizont_v2.addWidget(self.to_date)

        self.setMinimumSize(1000, 1000)

        self.info = QPushButton('Save')
        self.first_horizont.addWidget(self.info)
        self.info.clicked.connect(self.save_info)

        self.cb = QCheckBox('Deadline on/off', self)
        self.cb.stateChanged.connect(self.change_variable)
        self.first_horizont_v2.addWidget(self.cb)

        if os.path.getsize(filename) > 0:
            self.load_info()
        if os.path.getsize(finish_to_date_json) > 0:
            self.load_deadlines()
            self.check_cards_deadlines()

    def change_variable(self, state):
        if state == Qt.Checked:
            self.on_off = 'Enabled'
            print(self.on_off)
        else:
            self.on_off = 'Disabled'
            print(self.on_off)

    def add_card(self):
        self.second_class = custom_widget(self)
        label = self.second_class
        label.onTextChanged(self.entry.text())
        self.entry.setText('')
        self.labels.append(label)
        layout = self.layout_in_h1
        layout.addWidget(label.frame)
        created = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        created_to_date = datetime.strptime(created, '%d/%m/%y %H:%M:%S')
        one_day = timedelta(days=1)
        label.add_time(created)
        if self.on_off == 'Enabled':
            default_deadline = created_to_date+one_day
            default_deadline_formatted = datetime.strftime(default_deadline, "%d/%m/%y %H:%M:%S")
            self.default_date_func(default_deadline_formatted)
        elif self.on_off == 'Disabled':
            self.default_date_func(self.to_date.text())

    def default_date_func(self, date):
        id = len(MyWindow.finish_to_date_dict)-1
        MyWindow.finish_to_date_dict[id+1] = f'{date}'
        self.to_date.setText('')

    def save_info(self):
        MyWindow.dictionary_of_cards.clear()
        widget_count1 = self.layout_in_h1.count()
        widget_count2 = self.layout_in_h2.count()
        widget_count3 = self.layout_in_h3.count()
        for i in range(widget_count1):
            MyWindow.dictionary_of_cards[i] = [self.layout_in_h1.itemAt(i).widget().findChildren(QLabel)[0].text(),
                                           self.layout_in_h1.itemAt(i).widget().findChildren(QLabel)[1].text(),
                                           'layout_in_h1', 1]
        for p in range(widget_count2):
            MyWindow.dictionary_of_cards[p+widget_count1] = [self.layout_in_h2.itemAt(p).widget().findChildren(QLabel)[0].text(),
                                           self.layout_in_h2.itemAt(p).widget().findChildren(QLabel)[1].text(),
                                           'layout_in_h2', 2]
        for k in range(widget_count3):
            MyWindow.dictionary_of_cards[k+widget_count1+widget_count2] = [self.layout_in_h3.itemAt(k).widget().findChildren(QLabel)[0].text(),
                                           self.layout_in_h3.itemAt(k).widget().findChildren(QLabel)[1].text(),
                                           'layout_in_h3', 3]
        with open(filename, 'w') as f:
            json.dump(MyWindow.dictionary_of_cards, f)
            print('cards have been saved')

    def finish_to_date(self):
        with open(finish_to_date_json, 'w') as f:
            json.dump(MyWindow.finish_to_date_dict, f)
            print('dates to have been saved')

    def load_deadlines(self):
        with open(finish_to_date_json, 'r') as f:
            MyWindow.finish_to_date_dict = json.load(f)

    def check_cards_deadlines(self):
        current = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        current_date = datetime.now().strptime(current, '%d/%m/%y %H:%M:%S')
        for key, value in MyWindow.finish_to_date_dict.items():
            if value == '':
                pass
            else:
                deadline = datetime.strptime(value, '%d/%m/%y %H:%M:%S')
                if deadline <= current_date:
                    trayIcon = QSystemTrayIcon(QIcon('icon.jpg'), parent=app)
                    trayIcon.setToolTip('Desktop Notification')
                    trayIcon.show()
                    trayIcon.showMessage('Card is overdue', f"Task: '{MyWindow.dictionary_of_cards[key][0]}' was due on {MyWindow.finish_to_date_dict[key]}"
                          f", it's on this board {MyWindow.dictionary_of_cards[key][2]}", QSystemTrayIcon.Information, 1000)

    def load_info(self):
        with open(filename, 'r') as f:
            MyWindow.dictionary_of_cards = json.load(f)
        list_of_layouts = [(values[0], values[1], values[2], values[3]) for (key, values) in MyWindow.dictionary_of_cards.items()]
        for i in range(len(MyWindow.dictionary_of_cards)):
            self.second_class = custom_widget(self)
            label = self.second_class
            label.onTextChanged(list_of_layouts[i][0])
            label.add_time(list_of_layouts[i][1])
            label.frame_counter = list_of_layouts[i][3]
            self.labels.append(label)
            if list_of_layouts[i][2] == 'layout_in_h1':
                self.layout_in_h1.addWidget(label.frame)
            elif list_of_layouts[i][2] == 'layout_in_h2':
                self.layout_in_h2.addWidget(label.frame)
            elif list_of_layouts[i][2] == 'layout_in_h3':
                self.layout_in_h3.addWidget(label.frame)

    def empty_json(self):
        with open(filename, 'w') as f:
            f.truncate(0)


class custom_widget:
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.frame_counter = 1

        self.frame = QFrame()
        self.frame.setFixedSize(220,70)
        self.frame.setStyleSheet("background-color: #F8F988; border: 1px solid #dcdcdc; border-radius: 3px;")
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
        self.button_done.clicked.connect(self.move_card)

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
        try:
            task_dict = self.frame.findChildren(QLabel)[0].text()
            date_dict = self.frame.findChildren(QLabel)[1].text()
            for key, value in MyWindow.dictionary_of_cards.items():
                if task_dict and date_dict in value:
                    del MyWindow.dictionary_of_cards[key]
                    if key in MyWindow.finish_to_date_dict:
                        del MyWindow.finish_to_date_dict[key]
                        final_dict = dict(zip(range(len(MyWindow.dictionary_of_cards)-1), list(MyWindow.finish_to_date_dict.values())))
                        MyWindow.finish_to_date_dict.clear()
                        MyWindow.finish_to_date_dict.update(final_dict)
                        print(MyWindow.finish_to_date_dict)
        except Exception as e:
            print(e)

    def move_card(self):
        if self.frame_counter == 3:
            self.frame_counter = 0
        next_frame = self.window.h_layout.itemAt(self.frame_counter).widget()
        next_frame.layout().addWidget(self.frame)
        self.frame_counter += 1

    def onTextChanged(self, text):
        self.label.setText(text)

    def add_time(self, date):
        self.label_date.setText(date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    # window.check_for_events()
    atexit.register(window.save_info)
    atexit.register(window.finish_to_date)
    sys.exit(app.exec_())
