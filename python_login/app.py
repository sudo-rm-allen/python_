import sqlite3

conn = sqlite3.connect('login.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user (
    id integer PRIMARY KEY,
    user text,
    pass text
            )""")



login = input('Enter user\n')
password = input('Enter password\n')
conpass = input('Confirm password\n')

while conpass != password :
    print('error password did not match\n')
    password = input('Enter password\n')
    conpass = input('Confirm password\n')

cur.execute("INSERT INTO user(user,pass) VALUES (?,?)",(login,password))
conn.commit()
cur.execute("SELECT * FROM user")
print(cur.fetchall())
conn.commit()
conn.close()

