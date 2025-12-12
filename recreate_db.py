import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'expenses.db')

# Delete the old database if it exists
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"Deleted old database: {DB_PATH}")

# Create new database with correct schema
with sqlite3.connect(DB_PATH) as c:
    c.execute("""
        CREATE TABLE expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            subcategory TEXT DEFAULT '',
            note TEXT DEFAULT '')
    """)
    print("Created new database with correct schema")
