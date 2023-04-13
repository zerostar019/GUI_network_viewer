from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from PyQt5.QtGui import QIcon

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(481, 303)
        Authorization.setMinimumSize(QtCore.QSize(481, 303))
        Authorization.setMaximumSize(QtCore.QSize(481, 303))
        Authorization.setWindowIcon(QIcon('logo.png'))
        Authorization.setStyleSheet("#Authorization{\n"
"    background-color: black;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Authorization)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 203, 185, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 441, 211))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setToolTipDuration(0)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    border-style: solid;\n"
"    padding: 1.5px;\n"
"    selection-background-color: darkgray;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
"#lineEdit_2:focus{\n"
"    font: 8pt \"Segoe UI\";\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    width: 70px;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setStyleSheet("font: 8pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 247, 244);\n"
"    border-radius: 10px;\n"
"    width: 100px;\n"
"    height: 30px;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
"#pushButton:hover{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: black;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 331, 61))
        self.label_3.setObjectName("label_3")
        Authorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)
        
        self.pushButton.clicked.connect(self.del_user)
        self.pushButton.clicked.connect(Authorization.close)


    def del_user(self):
        db = Database()
        ip = self.lineEdit_2.text().strip()
        db.delete_user(ip=ip)
        
    
        
        
        
        
    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Delete User"))
        self.lineEdit_2.setPlaceholderText(_translate("Authorization", "IP-адрес"))
        self.label.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Введите </span><span style=\" font-size:14pt; color:#000000;\">IP-адрес:</span></p></body></html>"))
        self.pushButton.setText(_translate("Authorization", "Удалить"))
        self.label_3.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Удаление пользователя</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Authorization = QtWidgets.QMainWindow()
    ui = Ui_Authorization()
    ui.setupUi(Authorization)
    Authorization.show()
    sys.exit(app.exec_())
