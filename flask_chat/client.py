import time
import sys
import requests

from PyQt5 import QtCore, QtGui, QtWidgets

from auth import UiAuth
from registration import UiReg
from chat_form import UiChat


class ReceiveThread(QtCore.QThread):
    receive_signal = QtCore.pyqtSignal(dict)

    def __init__(self, receive_info):
        super().__init__()
        self.receive_info = receive_info

    def run(self):
        while True:
            receive_msg = requests.post('http://127.0.0.1:5000/receive_message', json=self.receive_info).json()

            if receive_msg['messages'] != 'No message':
                self.receive_signal.emit(receive_msg)

            self.receive_info['last_time'] = time.time()
            time.sleep(5)


class AuthWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiAuth()
        self.ui.setupUi(self)

        self.ui.auth_reg_btn.clicked.connect(self.show_reg_window)
        self.ui.auth_join_btn.clicked.connect(self.check_user)
        
    def show_reg_window(self):
        self.close()
        self.reg_app = RegWindow()
        self.reg_app.show()

    def check_user(self):
        self.mail = self.ui.auth_mail_input.text()
        self.password = self.ui.auth_pass_input.text()
        self.auth_info = {
            'email': self.mail,
            'password': self.password
        }

        response = requests.post(
            'http://127.0.0.1:5000/authorization',
            json=self.auth_info).json()

        if len(response) != 1:
            self.hide()
            self.chat_app = ChatWindow(
                response['user_name'],
                response['user_id'],
                response['user_list']
            )
            self.chat_app.show()

        else:
            self.ui.auth_mail_input.clear()
            self.ui.auth_pass_input.clear()


class RegWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiReg()
        self.ui.setupUi(self)

        self.ui.reg_reg_btn.clicked.connect(self.reg_user)

    def reg_user(self):
        self.mail = self.ui.reg_mail_input.text()
        self.password = self.ui.reg_pass_input.text()
        self.name = self.ui.reg_name_input.text()
        self.reg_info = {
            'email': self.mail,
            'name': self.name,
            'password': self.password
        }

        response = requests.post('http://127.0.0.1:5000/registration', json=self.reg_info).json()

        self.close()
        self.chat_app = ChatWindow(
            response['user_name'],
            response['user_id'],
            response['user_list']
        )
        self.chat_app.show()


class ChatWindow(QtWidgets.QWidget):
    def __init__(self, user_name, user_id, user_list):
        super().__init__()
        self.ui = UiChat()
        self.ui.setupUi(self)

        self.user_name = user_name
        self.user_id = user_id
        self.user_list = user_list

        self.cur_receiver = ''
        self.last_receiver = ''
        self.time_req = {
            'user_id': self.user_id 
        }
        self.time = requests.post('http://127.0.0.1:5000/get_last_visit', json=self.time_req).json()
        self.last_visit_time = self.time['last_visit_time']

        self.ui.chat_users_list.addItems(self.user_list)
        self.ui.chat_send_btn.clicked.connect(self.send_message)
        self.ui.chat_users_list.itemClicked.connect(self.clear_browser)


    def start_receive_thread(self, receive_info):
        self.last_receiver = self.cur_receiver

        self.receive_thread = ReceiveThread(self.receive_info)
        self.receive_thread.receive_signal.connect(self.show_receive_msg)
        self.receive_thread.start()

    def stop_receive_thread(self):
        self.receive_thread.terminate()

    def show_receive_msg(self, res_message):
        self.res_message = res_message

        for msg in res_message['messages']:
            self.ui.chat_dialog_browser.append(f'{self.cur_receiver.upper()}:  {msg}')

    def send_message(self):
        self.message = self.ui.chat_msg_input.toPlainText()
        self.ui.chat_msg_input.clear()
        self.ui.chat_dialog_browser.append(f'ВЫ:  {self.message}')
        self.time = time.time()
        self.send_info = {
            'sender_id': self.user_id,
            'receiver': self.cur_receiver,
            'message': self.message,
            'time': self.time
        }

        requests.post('http://127.0.0.1:5000/send_message',
                      json=self.send_info)

    def clear_browser(self):
        self.ui.chat_msg_input.clear()
        self.ui.chat_dialog_browser.clear()
        self.cur_receiver = self.ui.chat_users_list.currentItem().text()

        if (self.cur_receiver != self.last_receiver and
            self.last_receiver != ''):
            self.stop_receive_thread()

        self.ui.chat_user_name.setText(self.cur_receiver)
        self.receive_info = {
            'sender': self.cur_receiver,
            'receiver_id': self.user_id,
            'last_time': self.last_visit_time
        }

        self.last_visit_time = time.time()
        self.start_receive_thread(self.receive_info)      

    def closeEvent(self,  event):
        self.time_req['time'] = time.time()
        requests.post('http://127.0.0.1:5000/add_last_visit',
                      json=self.time_req)
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    auth_app = AuthWindow()
    auth_app.show()   
    sys.exit(app.exec())
