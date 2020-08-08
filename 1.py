#SQLITE3 ALL WORKS.
import sqlite3
conn=sqlite3.connect("example1.db")#connection done

curobj=conn.cursor()#cursor obj created.

#creating table
curobj.execute('''CREATE TABLE STOCKS(
                    DATE TEXT, TRANS TEXT, SYMBOL TEXT, QTY REAL, PRICE REAL)''')
#Iinserting into table.
curobj.execute('''INSERT INTO STOCKS VALUES('2020-07-24','BUY','RHAT','100','35.14')''')

#save (commit) the changes.
conn.commit()

