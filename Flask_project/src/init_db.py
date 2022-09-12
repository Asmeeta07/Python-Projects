import sqlite3

db = sqlite3.connect("users.db")
cur = db.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS users(
   id integer PRIMARY KEY,
   name text NOT NULL,
   email text NOT NULL);''')
# id = 4
# email = "asmeeta.dew@gmail.com"
# name = "Asmeeta"
#
# cur.execute("INSERT INTO users VALUES (?, ?,? )", (id , name,email))
# db.commit()
#
# user = "Asmeeta"
# cur.execute("""SELECT name, email
#                            FROM users
#                            WHERE name=?""",
#                     (user,))
# rows = cur.fetchall()
# print(rows)

db.commit()
db.close()