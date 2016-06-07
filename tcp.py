import socket
import sys
import sqlite3
HOST = 'gump.gatech.edu'
PORT = 756
server_address = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

conn = sqlite3.connect('feeds.db')
c = conn.cursor()

def recvall(sock):
    data = ""
    part = None
    while 1:
        try:
            part_s=''
            part = sock.recv(2048)
            if '\n' in part:
            	print 'feed set'
            	parts= part_s+part
            	part_s=''
            	partsl=parts.split('\n')
            	for part in partsl:
            		print part
	            	partl= part.split(',')
	            	if len(partl)==6:
		            	bus= partl[1]
		            	lat=partl[2]
		            	lon=partl[3]
		            	c.execute("insert into FEEDS (bus, lat,lon) values (?, ?, ?)",(bus,lat,lon))
		            	conn.commit()
	        else:
	        	print 'partal feed'
            	part_s=part_s+part
        except ValueError:
            print "Oops!  That was not a valid number.  Try again..."

recvall(sock)
conn.close()
