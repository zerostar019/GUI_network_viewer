from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from database import Database
import password_hash

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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setStyleSheet("font: 8pt \"Segoe UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    border-style: solid;\n"
"    padding: 1.5px;\n"
"    selection-background-color: darkgray;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
"#lineEdit_3:focus{\n"
"    font: 8pt \"Segoe UI\";\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    width: 70px;\n"
"}")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setStyleSheet("font: 8pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(50, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox.setStyleSheet("#comboBox{\n"
"    background: transparent;\n"
"    border: 0.5px solid white;\n"
"    border-radius: 3px;\n"
"\n"
"}")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
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
        
        self.pushButton.clicked.connect(self.save_new_user)
        self.pushButton.clicked.connect(Authorization.close)
        
        
    def save_new_user(self):
        ip = self.lineEdit_2.text().strip()
        password = self.lineEdit_3.text().strip()
        root = self.comboBox.currentText().strip()
        
        if ip is None:
            pass
        elif password is None:
            pass
        elif root is None:
            pass
    
        else:
        
            pass_hash = password_hash.encrypt_password(password=password)
        
            db = Database()
        
            # save data
            db.insert__pass(ip=str(ip), password=password)
            db.insert_data(ip=str(ip), password=pass_hash[0], root=str(root))
            db.insert_salt(ip=str(ip), salt=pass_hash[1])
					
        
        

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "New User"))
        self.lineEdit_2.setPlaceholderText(_translate("Authorization", "IP-адрес"))
        self.label_2.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Введите п</span><span style=\" font-size:14pt; color:#000000;\">ароль:</span></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("Authorization", "Пароль"))
        self.label.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Введите </span><span style=\" font-size:14pt; color:#000000;\">IP-адрес:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Authorization", "1"))
        self.comboBox.setItemText(1, _translate("Authorization", "2"))
        self.comboBox.setItemText(2, _translate("Authorization", "3"))
        self.label_4.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Уровень д</span><span style=\" font-size:14pt; color:#000000;\">оступа:</span></p></body></html>"))
        self.pushButton.setText(_translate("Authorization", "Зарегистрировать"))
        self.label_3.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Регистрация нового пользователя</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Authorization = QtWidgets.QMainWindow()
    ui = Ui_Authorization()
    ui.setupUi(Authorization)
    Authorization.show()
    sys.exit(app.exec_())
