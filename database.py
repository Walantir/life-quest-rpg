import sqlite3

def init_db():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS checkins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL,
            sleep REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_checkin(weight, sleep):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO checkins (weight, sleep, date) VALUES (?, ?, date('now'))",
        (weight, sleep)
    )     
    conn.commit()
    conn.close()

def get_checkins():
    conn=sqlite3.connect('game.db')
    rows = conn.execute('SELECT * FROM checkins').fetchall()
    conn.close()
    return rows