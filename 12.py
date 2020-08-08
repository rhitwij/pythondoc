#Delete Records

#importing
import sqlite3

#connecting to database.
conn = sqlite3.connect("customer.db")

#create cursor.
c = conn.cursor()

#query database.
c.execute("""DELETE FROM customers WHERE rowid = 4""")

c.execute("""SELECT rowid, * from customers""")
items = c.fetchall()
for line in items:
    print(line)

#commit changes.
conn.commit()

#close the connection.
conn.close()