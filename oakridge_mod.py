import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from hospital_auto import *

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.conn = sqlite3.connect("oakridge.db")
        self.cursor = self.conn.cursor()
        self.buttonadd.clicked.connect(self.add)
        self.buttonsave.clicked.connect(self.save)
        self.buttonselect.clicked.connect(self.select)
        self.buttondelete.clicked.connect(self.delete)
        self.buttonsearch.clicked.connect(self.search)
        self.retrieve()
        
    def retrieve(self):
        try:
            self.cursor=self.conn.execute("select ID,Name,DOB,Illness from hospital")                                          
            all_rows=self.cursor.fetchall()
            self.lw.clear()
            showrow="ID" + "\t"+ "Name"+"\t"+"DOB"+"\t"+"Illness"+"\t"
            self.lw.addItem(showrow)
            for i in all_rows:
                ide,namep,dob,ill=i
                showrow=str(ide)+"\t"+namep+"\t"+dob+"\t"+ill+"\t"
                self.lw.addItem(showrow)
        except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occurred:",e.args[0])
        
