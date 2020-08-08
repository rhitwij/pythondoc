#and or or

#importing
import sqlite3

#connecting to database.
conn = sqlite3.connect("customer.db")

#create cursor.
c = conn.cursor()

#query the database.
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Kh%' AND rowid = 3")
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Kh%' OR rowid = 3")
items = c.fetchall()
for line in items:
    print(line)


#commit changes
conn.commit()
#close the connection.
conn.close()