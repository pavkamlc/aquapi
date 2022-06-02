from distutils.util import execute
import os
import sqlite3

dbfile = r'db\aquapi.sqlite'
connection = sqlite3.Connection

# if database not found
if not os.path.isfile(dbfile):
    createdb()
    initdb()

def createdb():
        connection = sqlite3.connect(dbfile)
        with open(r'db\schema.sql') as f:
            connection.executescript(f.read())
        connection.commit()
        connection.close()
    
def initdb():
    # if first run app or reset to default   
    connection = sqlite3.connect(dbfile) 
    cursor = connection.cursor()

    admincount = cursor.execute("select count(username) from users where username='admin'")
    if admincount.fetchone()[0] <= 0:
        with open(r'db\default.sql') as f:
            connection.executescript(f.read())

    connection.commit()
    connection.close()

def dbgetconfig():
    config = 1;
    return

def dbputconfig(config)
    connection = sqlite3.connect(dbfile) 
    cursor = connection.cursor()

    cursor.execute("insert or replace into Book (ID, Name, TypeID, Level, Seen) values ((select ID from Book where Name = 'SearchName'), 'SearchName', ...);")
    
    connection.commit()
    connection.close()



