# Form implementation generated from reading ui file 'c:\Users\Kompik\Desktop\nd 12 Dima\Qtdesigner\ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.generate_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(60, 190, 75, 23))
        self.generate_btn.setStyleSheet("color:red;\n"
"background:white;\n"
"border: 1px solid black")
        self.generate_btn.setObjectName("generate_btn")
        self.use_numbers = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.use_numbers.setGeometry(QtCore.QRect(10, 120, 151, 17))
        self.use_numbers.setObjectName("use_numbers")
        self.use_letters = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.use_letters.setGeometry(QtCore.QRect(10, 150, 151, 20))
        self.use_letters.setStyleSheet("color:blue;\n"
"border:1px solid black;")
        self.use_letters.setObjectName("use_letters")
        self.result = QtWidgets.QLabel(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Генератор паролів"))
        self.generate_btn.setText(_translate("MainWindow", "Сгенерувати"))
        self.use_numbers.setText(_translate("MainWindow", "Використовувати числа"))
        self.use_letters.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))
