import sqlite3

con=sqlite3.connect(":memory:")
con.isolation_level=None
curobj=con.cursor()

buffer=""

print("Enter your sql commmand to execute in sqlite3")
print("Enter a blank line to exit")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            curobj.execute(buffer)

            if buffer.lstrip().upper().startswith('SELECT'):
                print(curobj.fetchall())
        except sqlite3.Error as e:
            print("An error occurred: ", e.args[0])
        buffer = ""
con.close()
