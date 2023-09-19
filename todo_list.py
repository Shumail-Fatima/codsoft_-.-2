from PyQt5 import QtCore, QtGui, QtWidgets

lst = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 226, 176);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.headlabel = QtWidgets.QLabel(self.centralwidget)
        self.headlabel.setGeometry(QtCore.QRect(190, 70, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(43)
        self.headlabel.setFont(font)
        self.headlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headlabel.setObjectName("headlabel")
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.addButton.setGeometry(QtCore.QRect(50, 230, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.addButton.setObjectName("addButton")
        
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.deleteButton.setGeometry(QtCore.QRect(50, 320, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.deleteButton.setObjectName("deleteButton")
        
        self.task_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.task_listWidget.setGeometry(QtCore.QRect(370, 260, 301, 261))
        self.task_listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_listWidget.setLineWidth(25)
        self.task_listWidget.setObjectName("task_listWidget")
        
        self.checkButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.check_it())
        self.checkButton.setGeometry(QtCore.QRect(50, 410, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.checkButton.setFont(font)
        self.checkButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.checkButton.setObjectName("checkButton")
        
        self.task_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.task_lineEdit.setGeometry(QtCore.QRect(370, 190, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(10)
        self.task_lineEdit.setFont(font)
        self.task_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_lineEdit.setText("")
        self.task_lineEdit.setObjectName("task_lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def add_it(self):
        item = self.task_lineEdit.text()
        lst.append(item)
        #print (lst)
        self.task_listWidget.addItem(item)
        self.task_lineEdit.setText("")

    def delete_it(self):
        selected = self.task_listWidget.currentRow()
        self.task_listWidget.takeItem(selected)

    def check_it(self):
        #pass
        selected = self.task_listWidget.currentRow()
        task = lst [selected]
        new = f'{task}{"  checked as done!"}'
        self.task_listWidget.takeItem(selected)
        self.task_listWidget.addItem(new)

        #print (new)
        #print(selected)
        #self.task_listWidget.setCurrentItem()
        #lst = [selected]

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headlabel.setText(_translate("MainWindow", "To-Do List"))
        self.addButton.setText(_translate("MainWindow", "Add Task"))
        self.deleteButton.setText(_translate("MainWindow", "Delete task"))
        self.checkButton.setText(_translate("MainWindow", "Check task as done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
