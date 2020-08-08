import sqlite3

#connect to database.
conn = sqlite3.connect("customer.db")

#create a cursor
c = conn.cursor()

many_customers = [('Bill','Gates','Billgates.com'),
                  ('Salman','Khan','Nepotism.com'),
                  ('Sameer','Dxit','baklol.com')]

#single values input.
#c.execute("INSERT INTO customers VALUES ('Roni','Mukherjee','roni@gmail.com')")

#multiple value input.
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

#commit our command
conn.commit()

#close our connection.
conn.close()