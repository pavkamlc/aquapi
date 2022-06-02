from distutils.util import execute
import os
import sqlite3

dbfile = r'db\aquapi.sqlite'
connection = sqlite3.Connection

# if database not found
if not os.path.isfile(dbfile):
    connection = sqlite3.connect(dbfile)
    with open(r'db\schema.sql') as f:
        connection.executescript(f.read())
    
# if first run app or reset to default   
connection = sqlite3.connect(dbfile) 
cursor = connection.cursor()
admincount = cursor.execute("select count(username) from users where username='admin'")
if admincount.fetchone()[0] <= 0:
    with open(r'db\default.sql') as f:
        connection.executescript(f.read())

connection.commit()
connection.close()
