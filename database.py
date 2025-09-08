import sqlite3

def init_db():
    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS packets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        src TEXT, dst TEXT, proto TEXT,
        sport INTEGER, dport INTEGER, length INTEGER
    )""")
    conn.commit()
    return conn, cursor

def log_packet(cursor, conn, src, dst, proto, sport, dport, length):
    cursor.execute("INSERT INTO packets (src, dst, proto, sport, dport, length) VALUES (?, ?, ?, ?, ?, ?)",
                   (src, dst, proto, sport, dport, length))
    conn.commit()
