from database import Database
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QIcon
import sys, os, hashlib
from auth_ui import Ui_Authorization
import password_hash


# Start desktop application
def start_app():
    # Application of authorization
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Authorization()
    ui.setupUi(window)
    window.setWindowIcon(QIcon('logo.png'))
    
    
    
    # Get data from input forms
    def get_input_data():
        
        # connect to database
        db = Database()
        
        # get login and password from form
        login = ui.lineEdit_2.text().strip()
        password = ui.lineEdit_3.text().strip()
        
        # get login and salt from database
        old_password = db.get_password(ip=str(login))[0][0]
        salt = db.get_salt(ip=str(login))[0][0]
        
               
        # check for registrated users
        try:
            if db.get_value(ip=str(login))[0][0] == 1:
                if password_hash.check_password(new_password=str(password), old_password=old_password, salt=salt) == True:
                    ui.open_admin(Authorization=window)
                else:
                    msg_window(IP=login, password=password, msg="s")
                    
            elif db.get_value(ip=str(login))[0][0] == 2:
                if password_hash.check_password(new_password=str(password), old_password=old_password, salt=salt) == True:
                    ui.open_ss(Authorization=window)
                else:
                    msg_window(IP=login, password=password, msg="sd")
            
            elif db.get_value(ip=str(login))[0][0] == 3:
                if password_hash.check_password(new_password=str(password), old_password=old_password, salt=salt) == True:
                    ui.open_s(Authorization=window)
                else:
                    msg_window(IP=login, password=password, msg="sd")
        except:
            msg_window(IP=login, password=password, msg="login")
        
        
        
    def msg_window(IP, password, msg):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(2)
        msg.setWindowIcon(QIcon('logo.png'))
        msg.setWindowTitle("Information")
        if msg == "login":
            msg.setText(f"Пользователь с IP-адресом {IP} не найден")
        else:
            msg.setText(f"{IP}\nБыл введен неправильный пароль!")
        msg.exec_()
        
        
        
    ui.pushButton.clicked.connect(get_input_data)
    
    window.show()
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    start_app()
    