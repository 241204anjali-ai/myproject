import sqlite3

def add_contact_to_db(name, phone, email, address):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?,?,?,?)",
                (name, phone, email, address))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_contact_from_db(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_contact_by_id(id):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE id=?", (id,))
    contact = cur.fetchone()
    conn.close()
    return contact

def update_contact_in_db(id, name, phone, email, address):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                (name, phone, email, address, id))
    conn.commit()
    conn.close()
