import sqlite3


class Database(object):
    def __init__(self):
        self.connection = sqlite3.connect('Users.db')
        self.cursor = self.connection.cursor()
    
        
    def get_data(self):
        return self.cursor.execute('''SELECT IP, Root FROM root''').fetchall()    
    
        
    def get_value(self, ip):
        return self.cursor.execute('''SELECT Root FROM root WHERE IP = ?''', (ip,)).fetchall()
        
        
    def insert_data(self, ip, password, root):
        self.cursor.execute('''INSERT INTO root(IP, Password, Root) VALUES(?, ?, ?)''', (
            ip,
            password,
            root,
        ))
        self.connection.commit()
        
        
    def insert_salt(self, ip, salt):
        self.cursor.execute('''INSERT INTO pass_salt(IP, Salt) VALUES(?, ?)''', (ip, salt,))
        self.connection.commit()
        
        
    def get_salt(self, ip):
        return self.cursor.execute('''SELECT Salt FROM pass_salt WHERE IP = ?''', (ip,)).fetchall()
           
        
    def get_password(self, ip):
        return self.cursor.execute('''SELECT PASSWORD FROM root WHERE IP = ?''', (ip,)).fetchall()
    
    
    def insert__pass(self, ip, password):
        self.cursor.execute('''INSERT INTO pass_users(IP, Password) VALUES(?, ?)''', (ip, password,))
        self.connection.commit()    
        
    def delete_user(self, ip):
        self.cursor.execute('''DELETE FROM root WHERE IP = ?''', (ip,))
        self.cursor.execute('''DELETE FROM pass_salt WHERE IP = ?''', (ip,))
        self.cursor.execute('''DELETE FROM pass_users WHERE IP = ?''', (ip,))
        self.connection.commit()

