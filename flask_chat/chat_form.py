# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UiChat(object):
    def setupUi(self, CHAT):
        CHAT.setObjectName("CHAT")
        CHAT.resize(480, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CHAT.sizePolicy().hasHeightForWidth())
        CHAT.setSizePolicy(sizePolicy)
        CHAT.setMinimumSize(QtCore.QSize(480, 480))
        CHAT.setMaximumSize(QtCore.QSize(480, 480))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 166, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 166, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 166, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 166, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        CHAT.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        CHAT.setFont(font)
        CHAT.setStyleSheet("QTextBrowser {\n"
"    background-color: #fff;\n"
"    border: 1px solid #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: #fff;\n"
"    border: 1px solid #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QListWidget::Item {\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QListWidget::Item:selected {\n"
"    background-color: #5181b8;\n"
"    border: none;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #fff;\n"
"    border: 1px solid #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar:vertical {              \n"
"            border: none;\n"
"            background: #fff;\n"
"            width: 5px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(81, 129, 184), stop: 0.5 rgb(81, 129, 184), stop:1 rgb(81, 129, 184));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(81, 129, 184), stop: 0.5 rgb(81, 129, 181),  stop:1 rgb(81, 129, 184));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(81, 129, 184), stop: 0.5 rgb(81, 129, 184),  stop:1 rgb(81, 129, 184));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.chat_msg_label = QtWidgets.QLabel(CHAT)
        self.chat_msg_label.setGeometry(QtCore.QRect(12, 341, 173, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.chat_msg_label.setFont(font)
        self.chat_msg_label.setObjectName("chat_msg_label")

        self.chat_dialog_browser = QtWidgets.QTextBrowser(CHAT)
        self.chat_dialog_browser.setGeometry(QtCore.QRect(10, 40, 340, 290))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.chat_dialog_browser.setFont(font)
        self.chat_dialog_browser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chat_dialog_browser.setObjectName("chat_dialog_browser")

        self.chat_msg_input = QtWidgets.QTextEdit(CHAT)
        self.chat_msg_input.setGeometry(QtCore.QRect(10, 361, 340, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.chat_msg_input.setFont(font)
        self.chat_msg_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chat_msg_input.setObjectName("chat_msg_input")

        self.chat_send_btn = QtWidgets.QPushButton(CHAT)
        self.chat_send_btn.setGeometry(QtCore.QRect(360, 362, 110, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.chat_send_btn.setFont(font)
        self.chat_send_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid #5181b8;\n"
"    border-radius: 7px;\n"
"    background-color: #5181b8;\n"
"    color: #fff;\n"
"}")
        self.chat_send_btn.setObjectName("chat_send_btn")

        self.chat_users_label = QtWidgets.QLabel(CHAT)
        self.chat_users_label.setGeometry(QtCore.QRect(360, 18, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.chat_users_label.setFont(font)
        self.chat_users_label.setObjectName("chat_users_label")

        self.chat_user_name = QtWidgets.QTextBrowser(CHAT)
        self.chat_user_name.setGeometry(QtCore.QRect(15, 10, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.chat_user_name.setFont(font)
        self.chat_user_name.setStyleSheet("QTextBrowser {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.chat_user_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chat_user_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chat_user_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chat_user_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.chat_user_name.setObjectName("chat_user_name")
        
        self.chat_users_list = QtWidgets.QListWidget(CHAT)
        self.chat_users_list.setGeometry(QtCore.QRect(360, 40, 111, 291))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.chat_users_list.setObjectName("chat_users_list")

        self.retranslateUi(CHAT)
        QtCore.QMetaObject.connectSlotsByName(CHAT)

    def retranslateUi(self, CHAT):
        _translate = QtCore.QCoreApplication.translate
        CHAT.setWindowTitle(_translate("CHAT", "Form"))
        self.chat_msg_label.setText(_translate("CHAT", "НАПИСАТЬ СООБЩЕНИЕ:"))
        self.chat_msg_input.setHtml(_translate("CHAT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chat_send_btn.setText(_translate("CHAT", "ОТПРАВИТЬ"))
        self.chat_users_label.setText(_translate("CHAT", "ПОЛЬЗОВАТЕЛИ:"))
        self.chat_user_name.setHtml(_translate("CHAT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
