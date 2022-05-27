import sqlite3

connection = sqlite3.connect('aquapi.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO config (configname, configvalue) VALUES (?, ?)",
            ('mqtt_host', '127.0.0.1')
            )
            
cur.execute("INSERT INTO config (configname, configvalue) VALUES (?, ?)",
            ('mqtt_port', '1883')
            )

cur.execute("INSERT INTO users (username, userpassword) VALUES (?, ?)",
            ('admin', 'aquapi')
            )


connection.commit()
connection.close()