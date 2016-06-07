import sqlite3
import sched, time

conn = sqlite3.connect('feeds.db')
c = conn.cursor()
c.execute("select count(*) from FEEDS")
res=c.fetchone()
lastCount=res[0]
print lastCount
newFeedsCount=0

def getNewFeeds(sc): 
	global lastCount
	c.execute("select count(*) from FEEDS")
	res=c.fetchone()
	newFeedsCount=res[0]-lastCount
	if newFeedsCount>0 :
		lastCount=res[0]
		print newFeedsCount
		c.execute("select * from FEEDS limit "+ str(newFeedsCount)+' OFFSET (SELECT COUNT(*) FROM FEEDS)-10')
		res=c.fetchall()
		f=open('newFeeds.json','w')
		st='{"buses":['
		for row in res:
			print ','.join(row)  
			st=st+'{"number":'+row[0]+',"lat":'+row[1]+',"lon":'+row[2]+'},\n'
		st=st+'{}]}'
		f.write(st)
		f.close()

	sc.enter(1, 1, getNewFeeds, (sc,))


s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, getNewFeeds, (s,))
s.run()




