import psycopg2

psy_conn = "dbname='database1' user='postgres' password='********' host='localhost' port='5432' "

def create_table():
    conn=psycopg2.connect(psy_conn)

    cur=conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_data(item,quantity,price):
        conn=psycopg2.connect(psy_conn)
        cur=conn.cursor()

        cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
        conn.commit()
        conn.close()

def view_data():
    conn=psycopg2.connect(psy_conn)
    cur=conn.cursor()

    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn=psycopg2.connect(psy_conn)
    cur=conn.cursor()

    cur.execute('DELETE FROM store WHERE item=%s',(item,))
    conn.commit()
    conn.close()

def update_data(quantity,price,item):
    conn=psycopg2.connect(psy_conn)
    cur=conn.cursor()

    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s',(quantity,price,item))
    conn.commit()
    conn.close()

# print(view_data())

create_table()

# insert_data('Apple',10,1.00)

print(view_data())

#It would be better to add IDs to all items so you can use ID numbers instead of item names when doing queries.
