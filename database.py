# database.py
import sqlite3
from config import DB_PATH

def connect_db():
    return sqlite3.connect(DB_PATH)

def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(user_id, username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
