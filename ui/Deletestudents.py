# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Deletestudents.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from 数据库课程设计.ui import images_rc
from 数据库课程设计.str import adminOp
from 数据库课程设计.ui import delsuccess

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        self.setWindowIcon(QIcon(':images/tubiao.png'))
        Dialog.setObjectName("MainWindow")
        Dialog.resize(800, 600)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Deletestudents)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 281, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(142, 130, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Deletestudents(self):
        if adminOp.delStu(int(self.lineEdit.text())):
            self.hide()
            self.f = delsuccess.Ui_Dialog()
            self.f.show()
        else:
            QMessageBox.warning(self, '错误', '没有该学生', QMessageBox.Yes | QMessageBox.No)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "删除信息"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "请输入要删除的学生学号"))
        self.label_2.setText(_translate("Dialog", "学号："))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Dialog()
    w.show()
    sys.exit(app.exec_())
