from datetime import date
import sqlite3
import unicodedata


con = sqlite3.connect('UserList.db')
cur = con.cursor()


class User:
    today = date.today()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def username(self):
       
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        self.name = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', self.name).translate(trans_tab))
        self.surname = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', self.surname).translate(trans_tab))
        
        if len(self.name) > 6:
            return self.name[:4] + self.surname[:4] + str(User.today.day) + str(User.today.year)[2:]
        elif len(self.name) <= 6 and len(self.name) > 4: 
            return self.name + self.surname[:2] + str(User.today.day) + str(User.today.year)[2:]
        else:
            return self.name + self.surname[:4] + str(User.today.day) + str(User.today.year)[2:]
        

    

            
class Database:
    
    def __init__(self, name, surname, area, username, vm):
        self.name = name
        self.surname = surname
        self.area = area
        self.username = username
        self.vm = vm
    
    @classmethod
    def create_table(cls):
        cur.execute("CREATE TABLE IF NOT EXISTS users(name text, surname text, area text, username text PRIMARY KEY, vm varchar)")
        con.commit()

    
    def put_in(self):
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (self.name, self.surname, self.area, self.username, self.vm))
        con.commit() 

    
    @staticmethod
    def delete(username):
        cur.execute("DELETE FROM users WHERE username = ?;", [username])
        print("Usuario eliminado correctamente: " + str(con.total_changes))
        con.commit()


    @staticmethod
    def get_user(username):
        cur.execute("SELECT * FROM users WHERE username = ?;", [username])
        registro = cur.fetchall()
        if registro:
            for row in registro:
                print("Nombre: ", row[0])  
                print("Apellido: ", row[1])
                print("Área: ", row[2])
                print("Nombre de Usuario: ", row[3])  
                print("Nombre de la Máquina Virtual: ", row[4])
        else:
            print("No existe el usuario!") 