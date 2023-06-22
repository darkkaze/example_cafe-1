import sqlite3

def crear_db():
    conn = sqlite3.connect('cafeteria.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telefono TEXT
        )
    ''')
    conn.close()