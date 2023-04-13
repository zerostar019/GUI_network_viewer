from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from database import Database
from PyQt5.QtWidgets import QTableWidgetItem
from reg_form import Ui_Authorization
from del_form import Ui_Authorization as DeleteForm

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 584)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(471, 584))
        Form.setMaximumSize(QtCore.QSize(471, 584))
        Form.setWindowIcon(QIcon('logo.png'))
        Form.setStyleSheet("#Form {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 203, 185, 255), stop:1 rgba(255, 255, 255, 255));\n"
    "    border: 3px solid white;\n"
    "    border-radius: 10px;\n"
    "}")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(140, 20, 311, 531))
        self.tableWidget.setStyleSheet("#tableWidget{\n"
    "    border: 3px solid white;\n"
    "    border-radius: 5px;\n"
    "    \n"
    "}\n"
    "#tableWidget:focus{\n"
    "    border: 0.5px solid black;\n"
    "    border-radius: 5px;\n"
    "}\n"
    "")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("#pushButton{\n"
    "    background-color: transparent;\n"
    "    border: 1px solid white;\n"
    "    border-radius: 5px;\n"
    "    font: 10pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "}\n"
    "#pushButton:hover{\n"
    "    background-color:  rgb(255, 204, 0);\n"
    "    font: 12pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "    color: red;\n"
    "    border: 0px;\n"
    "}")
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 20, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/photo/—Pngtree—vector signal tower wireless network_4402680.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 360, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
    "    background-color: transparent;\n"
    "    border: 1px solid white;\n"
    "    border-radius: 5px;\n"
    "    font: 10pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "}\n"
    "#pushButton_2:hover{\n"
    "    background-color: rgb(255, 0, 0);\n"
    "    font: 12pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "    border: 0px;\n"
    "    color: yellow;\n"
    "}")
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 290, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
    "    background-color: transparent;\n"
    "    border: 1px solid white;\n"
    "    border-radius: 5px;\n"
    "    font: 10pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "}\n"
    "#pushButton_3:hover{\n"
    "    background-color: rgb(0, 85, 255);\n"
    "    font: 12pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "    color: black;\n"
    "    border: 0px;\n"
    "}")
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 430, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
    "    background-color: transparent;\n"
    "    border: 1px solid white;\n"
    "    border-radius: 5px;\n"
    "    font: 10pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "}\n"
    "#pushButton_4:hover{\n"
    "    font: 12pt \'Times New Roman\';\n"
    "    font: bold;\n"
    "    color: black;\n"
    "    border: 0px;\n"
    "}")
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 80)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        self.load_data()
        self.pushButton.clicked.connect(self.register_user)
        self.pushButton_3.clicked.connect(self.refresh)
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.del_user)
        
    def del_user(self):
        self.Delete = QtWidgets.QMainWindow()
        self.del_ui = DeleteForm()
        self.del_ui.setupUi(self.Delete)
        self.Delete.show()
        
        
        
    def refresh(self):
        self.load_data()    
        
    def register_user(self):
        self.Authorization = QtWidgets.QMainWindow()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self.Authorization)
        self.Authorization.show()
        
        
    def load_data(self):
        db = Database()
        data = db.get_data()
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number, ip in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(ip)))
            

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "IP-адрес"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Права"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.pushButton_3.setText(_translate("Form", "Обновить"))
        self.pushButton_4.setText(_translate("Form", "Выйти"))

import res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
