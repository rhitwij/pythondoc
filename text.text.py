#not do this.
#SYMBOL='RHAT'
#C.execute("SELECT * FROM STOCKS WHERE SYMBOL='%S'" % SYMBOL)

#do this instead.
#t=('RHAT')
#c.execute("SELECT * FROM STOCKS WHERE SYMBOL = ?",t)
#print(c.fetchone())

#for larger examples.
#purchases = [('2020-07-24','BUY','RHAT','100','35.14'),('2020-07-25','SELL','HAT','100','35.14')]
#c.executemany('INSERT INTO STOCKS VALUES (?,?)',purchases)

