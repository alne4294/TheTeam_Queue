import sqlite3
from collections import deque

class EntryList:
	databaseFilename = "./entries.sqlite3"
	tableName = "Entries"
	tableFormat = "(eid TEXT PRIMARY KEY, subtime TEXT, course TEXT, helped TEXT, location TEXT, duration INT, helpedby TEXT)"

	def __init__(self, obj=None):
		conn = sqlite3.connect(self.databaseFilename)
		cur = conn.cursor()
		sql = 'create table if not exists ' + self.tableName + self.tableFormat
		cur.execute(sql)
		conn.commit()
		self.queue = deque()
		conn.close()

	def add(self, obj):
		self.queue.append(obj)
		#add to db
		try:
			conn = sqlite3.connect(self.databaseFilename)
			cur = conn.cursor()
			sql = 'insert into ' + self.tableName + ' values (' + self.objToDB(obj) + ');'
			cur.execute(sql)
			conn.commit()
			conn.close()
		except:
			return "error"


	def objToDB(self, obj):
		# should be in tableFormat with (x,x,'yyz') etc
		eid = str(obj.eid)
		subtime = str(obj.subTime)
		course = obj.course
		helped = str(obj.helped)
		location = obj.location
		duration = str(obj.duration)
		helpedBy = obj.helpedBy
		return self.wrapString(eid) + ', ' + self.wrapString(subtime) + ', ' + self.wrapString(course) + ', ' + self.wrapString(helped) + ', '+ self.wrapString(location) + ', ' + duration + ', ' + self.wrapString(helpedBy)

	def wrapString(self, s):
		return '\'' + s + '\''

	def modify(self, obj):
		if self.remove(obj.eid) == True:
			sql = "delete from " + self.tableName + " * where eid = " + self.wrapString(obj.eid) + ";"
			conn = sqlite3.connect(self.databaseFilename)
			cur = conn.cursor()
			cur.execute(sql)
			conn.commit()
			conn.close()
			self.appendLeft(obj)

	def remove(self, eid, duration = -1):
		for item in self.queue:
			if item.eid == eid:
				if duration != -1:
					item.duration = duration
				self.queue.remove(item)
				return True
		return False # Wasn't found

	def getById(self, x):
		for item in self.queue:
			if item.eid == x:
				return item
		return None

	def getByPos(self, x):
		if x > len(self.queue) or x < 0:
			return None
		return self.queue[x]

	def getAll(self):
		return self.queue

	def __updateDB(self):
		# called every time queue is changed
		return None
