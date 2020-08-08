#ordering

#importing.
import sqlite3

#connecting to database.
conn = sqlite3.connect("customer.db")

#create cursor.
c = conn.cursor()

#query the database by order.
#c.execute("""SELECT rowid, * FROM customers ORDER BY rowid DESC""")#DESC for decending
c.execute("""SELECT rowid, * FROM customers ORDER BY last_name""")

items = c.fetchall()
for line in items:
    print(line)
#commit changes.
conn.commit()
#close the connection
conn.close()