import sqlite3

def create_table():
    conn=sqlite3.connect('lite.db')

    cur=conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_data(item,quantity,price):
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()

        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
        conn.commit()
        conn.close()

def view_data():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()

    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()

    cur.execute('DELETE FROM store WHERE item=?',(item,))
    conn.commit()
    conn.close()

def update_data(quantity,price,item):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()

    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?',(quantity,price,item))
    conn.commit()
    conn.close()

print(view_data())

#It would be better to add IDs to all items so you can use ID numbers instead of item names when doing queries.
