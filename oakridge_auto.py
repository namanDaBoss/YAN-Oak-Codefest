# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oakridge.ui'
#
# Created: Sat Jan 23 17:05:43 2021
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(851, 583)
        MainWindow.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 127);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 231, 31))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(12, 28, 211);\n"
"font: 87 18pt \"Rockwell Extra Bold\";\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineid = QtGui.QLineEdit(self.centralwidget)
        self.lineid.setGeometry(QtCore.QRect(120, 130, 311, 21))
        self.lineid.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineid.setObjectName(_fromUtf8("lineid"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.linename = QtGui.QLineEdit(self.centralwidget)
        self.linename.setGeometry(QtCore.QRect(120, 160, 311, 21))
        self.linename.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.linename.setObjectName(_fromUtf8("linename"))
        self.linedob = QtGui.QLineEdit(self.centralwidget)
        self.linedob.setGeometry(QtCore.QRect(120, 190, 311, 21))
        self.linedob.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.linedob.setObjectName(_fromUtf8("linedob"))
        self.lineillness = QtGui.QLineEdit(self.centralwidget)
        self.lineillness.setGeometry(QtCore.QRect(120, 310, 311, 21))
        self.lineillness.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineillness.setObjectName(_fromUtf8("lineillness"))
        self.lw = QtGui.QListWidget(self.centralwidget)
        self.lw.setGeometry(QtCore.QRect(460, 130, 361, 341))
        self.lw.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lw.setObjectName(_fromUtf8("lw"))
        self.textpres = QtGui.QTextEdit(self.centralwidget)
        self.textpres.setGeometry(QtCore.QRect(120, 340, 311, 131))
        self.textpres.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textpres.setObjectName(_fromUtf8("textpres"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.linedov = QtGui.QLineEdit(self.centralwidget)
        self.linedov.setGeometry(QtCore.QRect(120, 280, 311, 21))
        self.linedov.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.linedov.setObjectName(_fromUtf8("linedov"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 100, 60, 16))
        self.label_8.setStyleSheet(_fromUtf8("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 127);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.linesearch = QtGui.QLineEdit(self.centralwidget)
        self.linesearch.setGeometry(QtCore.QRect(200, 100, 151, 21))
        self.linesearch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.linesearch.setObjectName(_fromUtf8("linesearch"))
        self.buttonadd = QtGui.QPushButton(self.centralwidget)
        self.buttonadd.setGeometry(QtCore.QRect(40, 490, 113, 32))
        self.buttonadd.setStyleSheet(_fromUtf8("\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttonadd.setObjectName(_fromUtf8("buttonadd"))
        self.buttonselect = QtGui.QPushButton(self.centralwidget)
        self.buttonselect.setGeometry(QtCore.QRect(370, 490, 113, 32))
        self.buttonselect.setStyleSheet(_fromUtf8("\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttonselect.setObjectName(_fromUtf8("buttonselect"))
        self.buttonsave = QtGui.QPushButton(self.centralwidget)
        self.buttonsave.setGeometry(QtCore.QRect(200, 490, 113, 32))
        self.buttonsave.setStyleSheet(_fromUtf8("\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttonsave.setObjectName(_fromUtf8("buttonsave"))
        self.buttondelete = QtGui.QPushButton(self.centralwidget)
        self.buttondelete.setGeometry(QtCore.QRect(540, 490, 113, 32))
        self.buttondelete.setStyleSheet(_fromUtf8("\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttondelete.setObjectName(_fromUtf8("buttondelete"))
        self.buttonclose = QtGui.QPushButton(self.centralwidget)
        self.buttonclose.setGeometry(QtCore.QRect(710, 490, 113, 32))
        self.buttonclose.setStyleSheet(_fromUtf8("\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttonclose.setObjectName(_fromUtf8("buttonclose"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 41, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 60, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineemail = QtGui.QLineEdit(self.centralwidget)
        self.lineemail.setGeometry(QtCore.QRect(120, 220, 311, 21))
        self.lineemail.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineemail.setObjectName(_fromUtf8("lineemail"))
        self.linephone = QtGui.QLineEdit(self.centralwidget)
        self.linephone.setGeometry(QtCore.QRect(120, 250, 311, 21))
        self.linephone.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.linephone.setObjectName(_fromUtf8("linephone"))
        self.buttonsearch = QtGui.QPushButton(self.centralwidget)
        self.buttonsearch.setGeometry(QtCore.QRect(220, 70, 101, 21))
        self.buttonsearch.setStyleSheet(_fromUtf8("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 127);\n"
"background-color: rgb(255, 255, 255);"))
        self.buttonsearch.setObjectName(_fromUtf8("buttonsearch"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Patient ID", None))
        self.label_2.setText(_translate("MainWindow", "Hospital Data", None))
        self.label_3.setText(_translate("MainWindow", "Patient Name", None))
        self.label_4.setText(_translate("MainWindow", "DOB", None))
        self.label_6.setText(_translate("MainWindow", "Patient illness", None))
        self.label_5.setText(_translate("MainWindow", "Prescription", None))
        self.label_7.setText(_translate("MainWindow", "Date of visits", None))
        self.label_8.setText(_translate("MainWindow", "Enter ID", None))
        self.buttonadd.setText(_translate("MainWindow", "ADD", None))
        self.buttonselect.setText(_translate("MainWindow", "SELECT", None))
        self.buttonsave.setText(_translate("MainWindow", "SAVE", None))
        self.buttondelete.setText(_translate("MainWindow", "DELETE", None))
        self.buttonclose.setText(_translate("MainWindow", "CLOSE", None))
        self.label_9.setText(_translate("MainWindow", "Email", None))
        self.label_10.setText(_translate("MainWindow", "Phone no.", None))
        self.buttonsearch.setText(_translate("MainWindow", "SEARCH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

