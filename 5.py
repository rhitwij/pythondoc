import sqlite3
#conn = sqlite3.connect(":memory:")# creats a connection to database in memory.

# Connection to the datbase
conn = sqlite3.connect("customer.db")

# create a cursor we use the cursor to do all kinds of things.
c = conn.cursor()

# create a table.
c.execute("""CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT
)""")

#Dataype:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB(img,mp4 file)

#save changes or commit changes.
conn.commit()

#close our connection.
conn.close()