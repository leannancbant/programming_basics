import sqlite3
import pathlib

DB_PATH = pathlib.Path(__file__).parent / "studieplanner.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_tables():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS modules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        naam TEXT NOT NULL,
        omschrijving TEXT NOT NULL
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

def add_testdata():
    with get_connection() as conn:
        conn.execute("INSERT INTO modules (naam, omschrijving) VALUES (?, ?)", ("Wiskunde", "Periode 1"))
        conn.execute("INSERT INTO modules (naam, omschrijving) VALUES (?, ?)", ("Programmeren", "Periode 2"))
        conn.execute("""
            INSERT INTO taken (omschrijving, deadline, geschatte_uren, prioriteit, modules_id)
            VALUES (?, ?, ?, ?, ?)
        """, ("Hoofdstuk 1 maken", "2026-12-01", 4, "Hoog", 1))

def get_modules():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM modules").fetchall()

if __name__ == "__main__":
    create_tables()