import sqlite3
import uuid

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
        self.name = name
        self.email = email
        self.password = password
        uid = str(uuid.uuid4())
        if self.check_uid(uid):
            ...
        else:
            self.add_user(self.name,self.email,self.password)

    def check_uid(self,uid):
        self.cur.execute("SELECT uid FROM users WHERE uid = ?",(uid,))
        if self.cur.fetchone() is None:
            return True
        return False
        

