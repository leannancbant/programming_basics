import sqlite3

def get_connection():
    conn = sqlite3.connect('studentplanner.db')
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_tables():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS modules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
        )
    """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS taken
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        omschrijving TEXT NOT NULL,
        deadline TEXT NOT NULL,
        geschatte_uren INTEGER NOT NULL,
        prioriteit TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Open',
        modules_id INTEGER NOT NULL,
        FOREIGN KEY (modules_id) REFERENCES modules (id)
        )
    """)

if __name__ == "__main__":
    create_tables()