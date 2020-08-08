#Format Results

import sqlite3


conn= sqlite3.connect("customer.db")

c = conn.cursor()

#query the database.
c.execute("SELECT * FROM customers")
#print(c.fetchone()[0])
#print(c.fetchmany())

items = c.fetchall()
for line in items:
    #print(line)
    #print(line[0]+" | "+line[1]+" | "+line[2])
    print(line[0] + " \t " + line[1] + " \t " + line[2])
conn.commit()

conn.close()