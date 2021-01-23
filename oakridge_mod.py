import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from oakridge_auto import *

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.conn = sqlite3.connect("oakridge.db")
        self.cursor = self.conn.cursor()
        self.buttonselect.clicked.connect(self.select)
        self.buttonadd.clicked.connect(self.add)
        self.buttonsave.clicked.connect(self.save)
        self.retrieve()
        self.sele="beginning"
        self.mode="notadd"
        self.select()

    def save(self):
        ido=self.lineid.text()
        pna=self.linename.text()
        pag=self.linedob.text()
        pil=self.lineemail.text()
        dat=self.linephone.text()
        des=self.linedov.text()
        illi=self.lineillness.text()
        pres=self.textpres.toPlainText()
        try:
            if self.mode=="notadd":  

                mysql="update hospital set Name='"+pna+"', DOB='"+pag+"', Email='"+pil+"', Phone="+dat+",Visit='"+des+"', Illness='"+ illi+"', Prescription='"+pres+"' where id="+str(ido)
                self.cursor=self.conn.execute(mysql)
                self.conn.commit()
                self.retrieve()
            elif self.mode=="adds":
                self.cursor=self.conn.execute("insert into hospital(Name,DOB,Email,Phone,Visit,Illness,Prescription)values \
                    (?,?,?,?,?,?,?)",(pna,pag,pil,int(dat),des,illi,pres))
                self.conn.commit()
                self.retrieve()
                self.mode="notadd"
        except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occurred:",e.args[0])
        self.retrieve()

    def add(self):
        self.lineid.setText("")
        self.linename.setText("")
        self.linedob.setText("")
        self.lineemail.setText("")
        self.linephone.setText("")
        self.linedov.setText("")
        self.lineillness.setText("")
        self.textpres.setText("")
        self.mode="adds"
        
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
                
    def select(self):
        if self.sele=="beginning":
            myrow=self.lw.item(1).text()
            li=myrow.split("\t")
            self.lineid.setText(li[0])
            try:
                self.cursor=self.conn.execute("select Name,DOB,Email,Phone,Visit,Illness,Prescription from hospital where id="+str(li[0]))
                row=self.cursor.fetchall()
                nem=row[0][0]
                dobi=row[0][1]
                emi=row[0][2]
                pho=row[0][3]
                vis=row[0][4]
                illi=row[0][5]
                pre=row[0][6]
                self.linename.setText(nem)
                self.linedob.setText(dobi)
                self.lineemail.setText(emi)
                self.linephone.setText(str(pho))
                self.linedov.setText(vis)
                self.lineillness.setText(illi)
                self.textpres.setText(pre)
            except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occurred:",e.args[0])                
                
            self.sele="afterwards"
        elif self.sele=="afterwards":    
            myrow=self.lw.item(self.lw.currentRow()).text()
            li=myrow.split("\t")
            self.lineid.setText(li[0])
            try:
                self.cursor=self.conn.execute("select Name,DOB,Email,Phone,Visit,Illness,Prescription from hospital where id="+str(li[0]))
                row=self.cursor.fetchall()
                nem=row[0][0]
                dobi=row[0][1]
                emi=row[0][2]
                pho=row[0][3]
                vis=row[0][4]
                illi=row[0][5]
                pre=row[0][6]
                self.linename.setText(nem)
                self.linedob.setText(dobi)
                self.lineemail.setText(emi)
                self.linephone.setText(str(pho))
                self.linedov.setText(vis)
                self.lineillness.setText(illi)
                self.textpres.setText(pre)
            except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occurred:",e.args[0])      
        
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()       
