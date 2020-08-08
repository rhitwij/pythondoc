import sqlite3


conn= sqlite3.connect("customer.db")

c = conn.cursor()

#query the database.
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany()
print(c.fetchall())

conn.commit()

conn.close()