import sqlite3
import os

DB_PATH = "database/cashflow.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_database():
    os.makedirs("database", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        name TEXT NOT NULL,
        category TEXT,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_date TEXT,
        total REAL,
        payment REAL,
        change_amount REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaction_details(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        price REAL,
        subtotal REAL,

        FOREIGN KEY(transaction_id)
        REFERENCES transactions(id),

        FOREIGN KEY(product_id)
        REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()