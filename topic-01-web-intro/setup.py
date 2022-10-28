import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Corn')")
cursor.execute("insert into list (description) values ('Potatoes')")
cursor.execute("insert into list (description) values ('Plate')")
cursor.execute("insert into list (description) values ('Glass')")
cursor.execute("insert into list (description) values ('Hoodies')")

connection.commit()
connection.close()

print("done.")
