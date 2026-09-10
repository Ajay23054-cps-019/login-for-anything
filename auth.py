import sqlite3
import uuid
import hashlib

class auth:
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    def __init__(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid TEXT PRIMARY KEY,
                name VARCHAR(50),
                email VARCHAR(100) UNIQUE,
                password VARCHAR(255)
            )
        """)
        self.conn.commit()

    def add_user(self,name,email,password):
        uid = str(uuid.uuid4())
        try:
            if self.check_uid(uid):
                self.cur.execute("INSERT INTO users (uid, name, email, password) VALUES (?,?,?,?)",(uid,name,email,self.hash_password(password)))
                self.conn.commit()
                return uid
            else:
                self.add_user(name,email,password)
        except:
            return "User already exists or invalid details"

    def check_uid(self,uid):
        self.cur.execute("SELECT uid FROM users WHERE uid = ?",(uid,))
        if self.cur.fetchone() is None:
            return True
        return False
        
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self,uid,password):
        self.cur.execute("SELECT password FROM users WHERE uid = ?",(uid,))
        result = self.cur.fetchone()
        if self.verify_login(password,result):
            return "HI"
        else:
            return "Bye"


    def verify_login(self,password,result):
        if self.hash_password(password) == result[0]:
            return True
        else:
            return False

a = auth()
print(a.add_user(name="Ajay",email="ajayhemanth90@gmail.com",password="Ajay@2008"))
print(a.login("47e6b712-b02a-4921-aa5c-dda38397a5ce","Ajay@2008"))