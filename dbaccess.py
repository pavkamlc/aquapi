#from distutils.util import execute
import os
import sqlite3
import bcrypt

dbfile = r'db\aquapi.sqlite'
connection = sqlite3.Connection

def createdb():
        connection = sqlite3.connect(dbfile)
        with open(r'db\schema.sql') as f:
            connection.executescript(f.read())
        connection.commit()
        connection.close()
    
def initdb():
    connection = sqlite3.connect(dbfile) 

    with open(r'db\default.sql') as f:
            connection.executescript(f.read())

    connection.commit()
    connection.close()

def dbgetconfig():
    connection = sqlite3.connect(dbfile) 
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("select * from config")
    config = cursor.fetchone()

    connection.commit()
    connection.close()

    return config

def dbputconfig(config):
    connection = sqlite3.connect(dbfile) 
    cursor = connection.cursor()
    print(config)
    cursor.execute("insert or replace into Book (ID, Name, TypeID, Level, Seen) values ((select ID from Book where Name = 'SearchName'), 'SearchName', ...);")

    connection.commit()
    connection.close()

def mypassword(mypassword):
    mysalt = bcrypt.gensalt()
    myhash = bcrypt.hashpw(mypassword, mysalt)

# if database not found
if not os.path.isfile(dbfile):
    createdb()
    initdb()

# if first run app or reset to default   
connection = sqlite3.connect(dbfile) 
cursor = connection.cursor()
admincount = cursor.execute("select count(username) from users where username='admin'")
if (admincount.arraysize) <= 0: 
    initdb()
