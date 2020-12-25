"""
Interacts with online database to send data back and forth

Database file
(Database.py)

:author Dallin Guisti
:version 1.0 - 27 Oct 2020
:python 3.9.0

"""

import hashlib
from dotenv.main import load_dotenv
import mariadb
import sys
from hashlib import sha256
import dotenv
import os


class Database:
    """
    Interacts with online database to send data back and forth
    """
    def __init__(self):
        """try:
            conn = mariadb.connect(
                user="scibowl",
                password="^@q&@8x1N*2X!0bN1&@51rdS*QXGIg",
                host = "192.168.68.128",
                port=3306,
                database="scibowl"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)"""
        
        #cur = self.getDB()
        #password = b"password12345"
        ##encrypted_password = hashlib.sha512(password).hexdigest()
        #cur.execute("INSERT INTO users (Username, Password, Email, Name, Level) VALUES (?, ?, ?, ?, ?)", ("dguisti", encrypted_password, "dguisti@davidsonacademy.unr.edu", "Dallin Guisti", "MS"))
        #cur.execute("SELECT * FROM users")
        #for (id, username, password, email, name, level) in cur:
        #    print(f"{id}: {name} identifies by {username} with the email {email} and a level of {level}")
    
    def getDB(self):
        load_dotenv()
        user = os.getenv("DBUSER")
        password = os.getenv("DBPASSWD")
        host = os.getenv("DBIP")
        port = int(os.getenv("DBPORT"))
        database = os.getenv("DBNAME")
        try:
            conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            conn.autocommit = True
            cur = conn.cursor()
            return cur
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return False

    def getUserData(self, uname):
        cur = self.getDB()
        cur.execute(f'SELECT * FROM users WHERE Username="{uname}"')
        return [y for y in cur][0]
    
    def getQuestionData(self, uname):
        cur = self.getDB()
        cur.execute(f'SELECT * FROM userstats WHERE Username="{uname}"')
        return [y for y in cur][0]

    def addUser(self,uname,passwd,email,name,level,rank):
        cur = self.getDB()
        if self.checkUserExist(uname) or self.checkEmailExist(email):
            return False
        
        encrypted_password = hashlib.sha512(passwd.encode("utf-8")).hexdigest()
        try:
            cur.execute("INSERT INTO users (Username, Password, Email, Name, Level, Rank) VALUES (?, ?, ?, ?, ?, ?)", (uname,encrypted_password,email,name,level,rank))
        except mariadb.Error as e:
            print("Error in adding user:", e)
            return False
        

    def checkUserExist(self,uname):
        cur = self.getDB()
        cur.execute(f"SELECT * FROM users WHERE Username='{uname}'")
        if len([y for y in cur]) > 0:
            return True
        else:
            return False

    def checkEmailExist(self,email):
        cur = self.getDB()
        cur.execute(f"SELECT * FROM users WHERE Email='{email}'")
        if len([y for y in cur]) > 0:
            return True
        else:
            return False

    def verifyUser(self, uname, passwd):
        if not self.checkUserExist(uname):
            return False
        cur = self.getDB()
        cur.execute(f"SELECT * FROM users WHERE Username='{uname}'")
        password = [y for y in cur][0][2]
        passwd_encrypted = hashlib.sha512(passwd.encode("utf-8")).hexdigest()
        if passwd_encrypted == password:
            return True
        return False

def main():
    myDatabase = Database()

if __name__ == "__main__":
    main()