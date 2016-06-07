#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('feeds.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE FEEDS(
       bus           TEXT,
       lat           TEXT,
       lon			TEXT);''')

#       ADDRESS        CHAR(50),
#       SALARY         REAL
print "Table created successfully";

conn.close()