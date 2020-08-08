#drop or delete tables
import sqlite3

conn =  sqlite3.connect("customer.db")

c = conn.cursor()

#drop table.
c.execute("DROP TABLE customers")
conn.commit()


c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for line in items:
    print(line)

conn.commit()

conn.close()