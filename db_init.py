import sqlite3
def init_db():
    conn = sqlite3.connect("grocery.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Database created successfully!")
if __name__ == "__main__":
    init_db()