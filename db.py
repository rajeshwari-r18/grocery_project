import sqlite3

DB = "grocery.db"

def _connect():
    return sqlite3.connect(DB)

def add_product(name, price, quantity):
    conn = _connect()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                  (name, price, quantity))
        conn.commit()
        return True, "Product added successfully!"
    except sqlite3.IntegrityError:
        return False, "Product name already exists!"
    finally:
        conn.close()

def get_all_products():
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_id(pid):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (pid,))
    row = c.fetchone()
    conn.close()
    return row

def update_product(pid, price=None, quantity=None):
    conn = _connect()
    c = conn.cursor()
    if price is not None:
        c.execute("UPDATE products SET price = ? WHERE id = ?", (price, pid))
    if quantity is not None:
        c.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, pid))
    conn.commit()
    conn.close()
    return "Product updated!"

def delete_product(pid):
    conn = _connect()
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (pid,))
    conn.commit()
    conn.close()
    return "Product deleted!"

def get_low_stock_products():
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE quantity < 5")
    rows = c.fetchall()
    conn.close()
    return rowsp

def search_products(keyword):
    conn = _connect()
    c = conn.cursor()
    # Search by name OR id
    c.execute("""
        SELECT * FROM products 
        WHERE name LIKE ? OR id LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    
    rows = c.fetchall()
    conn.close()
    return rows