# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UiReg(object):
    def setupUi(self, Reg):
        Reg.setObjectName("Reg")
        Reg.resize(410, 450)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Reg.setFont(font)
        Reg.setStyleSheet("QWidget {\n"
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
        self.reg_label = QtWidgets.QLabel(Reg)
        self.reg_label.setGeometry(QtCore.QRect(4, 20, 400, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(30)
        self.reg_label.setFont(font)
        self.reg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reg_label.setObjectName("reg_label")

        self.reg_name_label = QtWidgets.QLabel(Reg)
        self.reg_name_label.setGeometry(QtCore.QRect(10, 116, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.reg_name_label.setFont(font)
        self.reg_name_label.setObjectName("reg_name_label")

        self.reg_name_input = QtWidgets.QLineEdit(Reg)
        self.reg_name_input.setGeometry(QtCore.QRect(10, 139, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.reg_name_input.setFont(font)
        self.reg_name_input.setObjectName("reg_name_input")

        self.reg_mail_label = QtWidgets.QLabel(Reg)
        self.reg_mail_label.setGeometry(QtCore.QRect(10, 203, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.reg_mail_label.setFont(font)
        self.reg_mail_label.setObjectName("reg_mail_label")

        self.reg_mail_input = QtWidgets.QLineEdit(Reg)
        self.reg_mail_input.setGeometry(QtCore.QRect(10, 225, 380, 40))
        self.reg_mail_input.setObjectName("reg_mail_input")

        self.reg_pass_label = QtWidgets.QLabel(Reg)
        self.reg_pass_label.setGeometry(QtCore.QRect(10, 285, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.reg_pass_label.setFont(font)
        self.reg_pass_label.setObjectName("reg_pass_label")

        self.reg_pass_input = QtWidgets.QLineEdit(Reg)
        self.reg_pass_input.setGeometry(QtCore.QRect(10, 308, 380, 40))
        self.reg_pass_input.setObjectName("reg_pass_input")
        self.reg_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.reg_reg_btn = QtWidgets.QPushButton(Reg)
        self.reg_reg_btn.setGeometry(QtCore.QRect(54, 362, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.reg_reg_btn.setFont(font)
        self.reg_reg_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid #4bb34b;\n"
"    border-radius: 4px;\n"
"    background-color: #4bb34b;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0c9a0c;\n"
"}")
        self.reg_reg_btn.setObjectName("reg_reg_btn")

        self.retranslateUi(Reg)
        QtCore.QMetaObject.connectSlotsByName(Reg)

    def retranslateUi(self, Reg):
        _translate = QtCore.QCoreApplication.translate
        Reg.setWindowTitle(_translate("Reg", "Регистрация"))
        self.reg_label.setText(_translate("Reg", "РЕГИСТРАЦИЯ"))
        self.reg_name_label.setText(_translate("Reg", "NICKNAME:"))
        self.reg_mail_label.setText(_translate("Reg", "EMAIL:"))
        self.reg_pass_label.setText(_translate("Reg", "PASSWORD:"))
        self.reg_reg_btn.setText(_translate("Reg", "РЕГИСТРАЦИЯ"))
