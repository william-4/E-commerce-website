#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as schema:
    # execute multiple SQL statements at once
    connection.executescript(schema.read())

# process rows in the database
cursor = connection.cursor()

# add items to posts table
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('First Post', 'Content for the first post')
               )

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('Second Post', 'Content for the second post')
               )

connection.commit()
cursor.close()
connection.close()