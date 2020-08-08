#primary key id

#importing
import sqlite3
#connecting to the database.
conn = sqlite3.connect("customer.db")
#create a cursor.
c = conn.cursor()
#query the database.
c.execute("SELECT rowid, * FROM customers")#rowid is a default primary key.

items = c.fetchall()
for line in items:
    print(line)

#commit the changes
conn.commit()
#close the connection.
conn.close()