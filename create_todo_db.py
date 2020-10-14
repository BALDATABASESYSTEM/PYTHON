import sqlite3
conn = sqlite3.connect('todo.db') 
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, mission char(100) NOT NULL, is_active bool NOT NULL)")
conn.execute("INSERT INTO todo (mission,is_active) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
conn.execute("INSERT INTO todo (mission,is_active) VALUES ('Visit the Python website',1)")
conn.execute("INSERT INTO todo (mission,is_active) VALUES ('Test various editors for and check the syntax highlighting',1)")
conn.execute("INSERT INTO todo (mission,is_active) VALUES ('Choose your favorite WSGI-Framework',0)")
conn.commit()
