#RETRIVE AND DISPLAY DATA. SELECT

#importing package and connecting.
import sqlite3
conn=sqlite3.connect("example1.db")

#cursor obj created
curobj=conn.cursor()

#displaying row by row.
for row in curobj.execute("SELECT * FROM STOCKS ORDER BY PRICE"):
    print(row)

#save changes.
conn.commit()

#print(sqlite3.version_info)
#print(sqlite3.version)
#print(sqlite3.sqlite_version)
#print(sqlite3.PARSE_COLNAMES)
#print(sqlite3.PARSE_DECLTYPES)