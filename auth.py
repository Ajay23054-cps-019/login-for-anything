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
        if self.check_uid(uid):
            self.cur.execute("INSERT INTO users (uid, name, email, password) VALUES (?,?,?,?)",(uid,name,email,self.hash_password(password)))
            self.conn.commit()
        else:
            self.add_user(name,email,password)

    def check_uid(self,uid):
        self.cur.execute("SELECT uid FROM users WHERE uid = ?",(uid,))
        if self.cur.fetchone() is None:
            return True
        return False
        
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        ...

    def verify_login(self):
        ...