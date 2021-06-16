import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1, 'maxim', 'asdf')



insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)


users = [
    (2, 'roma', '123'),
    (3, 'sasha', 'asd'),
    (4, 'dima', 'qwe'),
    (5, 'liza', 'zxc'),
    (6, 'lesha', 'rty')
]

cursor.executemany(insert_query, users)

selecet_query = "SELECT * FROM users"
for row in cursor.execute(selecet_query):
    print(row)

connection.commit()

connection.close()
