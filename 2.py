#Data inserting.INSERT INTO
import sqlite3
conn=sqlite3.connect("example1.db")#connection done

curobj=conn.cursor()#cursor obj created.

#values stored in pur
pur = [('2020-07-30','BUY','HAT','100','45.14'),
      ('2020-07-25','SELL','RHAT','10','65.14'),
      ('2020-07-26','BUY','RHAT','50','35.14'),
      ('2020-07-27','SELL','RHAT','5','85.14'),
      ('2020-07-28','BUY','RHAT','1','75.14')]

#inserting values into table stocks.
curobj.executemany('INSERT INTO STOCKS VALUES (?,?,?,?,?)',pur)

#save the chages.
conn.commit()