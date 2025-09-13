import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()
