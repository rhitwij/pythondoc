#wher clause

#importing
import sqlite3

#connecting to database.
conn = sqlite3.connect("customer.db")

#create a cursor.
c = conn.cursor()

#query the database.
#c.execute("SELECT * FROM customers WHERE last_name = 'Khan'")
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'M%' ")
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com' ")#we can use logical operators as well in where clause.
items = c.fetchall()

for line in items:
    print(line)




#commit the change.
conn.commit()

#close the connection.
conn.close()