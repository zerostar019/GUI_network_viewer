from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(481, 180)
        Authorization.setMinimumSize(QtCore.QSize(481, 180))
        Authorization.setMaximumSize(QtCore.QSize(481, 180))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 361, 61))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 75, 23))
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
        Authorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)
        
        self.pushButton.clicked.connect(Authorization.close)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Information"))
        self.label_3.setText(_translate("Authorization", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Вам доступна информация уровня: </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">&quot;Секретно&quot;</span></p></body></html>"))
        self.pushButton.setText(_translate("Authorization", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Authorization = QtWidgets.QMainWindow()
    ui = Ui_Authorization()
    ui.setupUi(Authorization)
    Authorization.show()
    sys.exit(app.exec_())
