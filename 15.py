#limiting Result.

import sqlite3

conn =  sqlite3.connect("customer.db")

c = conn.cursor()

c.execute("SELECT rowid, * FROM customers LIMIT 2")

items = c.fetchall()
for line in items:
    print(line)





conn.commit()

conn.close()