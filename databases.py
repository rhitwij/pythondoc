import sqlite3


#Query database and return all records.
def show_all():
    # connecting database
    conn = sqlite3.connect("customer.db")
    # create cursor
    c = conn.cursor()

    #query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for line in items:
        print(line)
    #commit the changes.
    conn.commit()
    #close connection.
    conn.close()

#add a new record to the table.
def add_one(first,last,email):
    # connecting database
    conn = sqlite3.connect("customer.db")
    # create cursor
    c = conn.cursor()
    #insert query
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    # commit the changes.
    conn.commit()
    # close connection.
    conn.close()

#Delete a database
def delete_one(id):
    # connecting database
    conn = sqlite3.connect("customer.db")
    # create cursor
    c = conn.cursor()
    #delete query.
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    # commit the changes.
    conn.commit()
    # close connection.
    conn.close()

#Add many records.
def add_many(list):
    # connecting database
    conn = sqlite3.connect("customer.db")
    # create cursor
    c = conn.cursor()
    # insert query
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    # commit the changes.
    conn.commit()
    # close connection.
    conn.close()

#look up where.
def email_lookup(email):
    # connecting database
    conn = sqlite3.connect("customer.db")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE email = (?)",(email,))
    items = c.fetchall()

    for line in items:
        print(line)

    # commit the changes.
    conn.commit()
    # close connection.
    conn.close()


