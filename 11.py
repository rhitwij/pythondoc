#Update Records.

import sqlite3

#connect to database
conn = sqlite3.connect("customer.db")

#create cursor.
c = conn.cursor()

#Update records.
c.execute("""UPDATE customers SET first_name = 'Sameer ki chut'
        WHERE rowid ='4'
        """)
conn.commit()

#query the database.
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for line in items:
    print(line)




#commit the changes.
conn.commit()

#close the connection.
conn.close()