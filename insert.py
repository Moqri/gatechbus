import sqlite3

conn = sqlite3.connect('feeds.db')
name='aa'
phone='aa'
c = conn.cursor()
c.execute("insert into FEEDS (NAME, N2) values (?, ?)",
            (name, phone))
conn.commit()
conn.close()