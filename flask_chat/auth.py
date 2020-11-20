# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UiAuth(object):
    def setupUi(self, Auth):
        Auth.setObjectName("Auth")
        Auth.resize(410, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auth.sizePolicy().hasHeightForWidth())
        Auth.setSizePolicy(sizePolicy)
        Auth.setMinimumSize(QtCore.QSize(410, 430))
        Auth.setMaximumSize(QtCore.QSize(410, 430))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Auth.setFont(font)
        Auth.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(235,235,235,.2);\n"
"    border: 1px solid #1d65b7;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #fff;\n"
"    border: 1px solid #1d65b7;\n"
"    color: #1d65b7;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"}")
        self.auth_join_btn = QtWidgets.QPushButton(Auth)
        self.auth_join_btn.setGeometry(QtCore.QRect(10, 300, 150, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.auth_join_btn.setFont(font)
        self.auth_join_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid #5181b8;\n"
"    background-color: #5181b8;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1d65b7;\n"
"}")
        self.auth_join_btn.setObjectName("auth_join_btn")

        self.auth_reg_btn = QtWidgets.QPushButton(Auth)
        self.auth_reg_btn.setGeometry(QtCore.QRect(192, 300, 198, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.auth_reg_btn.setFont(font)
        self.auth_reg_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid #4bb34b;\n"
"    border-radius: 4px;\n"
"    background-color: #4bb34b;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0c9a0c;\n"
"}")
        self.auth_reg_btn.setObjectName("auth_reg_btn")

        self.auth_mail_input = QtWidgets.QLineEdit(Auth)
        self.auth_mail_input.setGeometry(QtCore.QRect(10, 139, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.auth_mail_input.setFont(font)
        self.auth_mail_input.setObjectName("auth_mail_input")

        self.auth_pass_input = QtWidgets.QLineEdit(Auth)
        self.auth_pass_input.setGeometry(QtCore.QRect(10, 225, 380, 40))
        self.auth_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.auth_pass_input.setFont(font)
        self.auth_pass_input.setObjectName("auth_pass_input")

        self.auth_mail_label = QtWidgets.QLabel(Auth)
        self.auth_mail_label.setGeometry(QtCore.QRect(10, 116, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.auth_mail_label.setFont(font)
        self.auth_mail_label.setStyleSheet("")
        self.auth_mail_label.setObjectName("auth_mail_label")

        self.auth_pass_label = QtWidgets.QLabel(Auth)
        self.auth_pass_label.setGeometry(QtCore.QRect(10, 200, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.auth_pass_label.setFont(font)
        self.auth_pass_label.setObjectName("auth_pass_label")

        self.auth_label = QtWidgets.QLabel(Auth)
        self.auth_label.setGeometry(QtCore.QRect(0, 20, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(30)
        self.auth_label.setFont(font)
        self.auth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auth_label.setObjectName("auth_label")

        self.retranslateUi(Auth)
        QtCore.QMetaObject.connectSlotsByName(Auth)

    def retranslateUi(self, Auth):
        _translate = QtCore.QCoreApplication.translate
        Auth.setWindowTitle(_translate("Auth", "Авторизация"))
        self.auth_join_btn.setText(_translate("Auth", "ВОЙТИ"))
        self.auth_reg_btn.setText(_translate("Auth", "РЕГИСТРАЦИЯ"))
        self.auth_mail_label.setText(_translate("Auth", "EMAIL:"))
        self.auth_pass_label.setText(_translate("Auth", "PASSWORD:"))
        self.auth_label.setText(_translate("Auth", "АВТОРИЗАЦИЯ"))
