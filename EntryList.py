import sqlite3
from collections import deque
from Entry import entry

class EntryList:
	databaseFilename = "./entries.sqlite3"
	tableName = "Entries"
	tableFormat = "(eid TEXT PRIMARY KEY, name TEXT, subtime TEXT, course TEXT, helped INT, location TEXT, duration INT, helpedby TEXT)"

	def __init__(self, obj=None):
		self.conn = sqlite3.connect(self.databaseFilename, check_same_thread=False)
		self.queue = deque()
		with self.conn:
			cur = self.conn.cursor()
			drop = "drop table if exists " + self.tableName
			#cur.execute(drop)
			sql = 'create table if not exists ' + self.tableName + self.tableFormat
			cur.execute(sql)
			self.conn.commit()

			cur.execute("select * from " + self.tableName + ";")
			while True:
				row = cur.fetchone()
				if row == None:
					break
				newObj = self.createEntry(row)
				self.queue.append(newObj)

	def createEntry(self, row):
		eid = row[0]
		name = row[1]
		subtime = row[2]
		course = row[3]
		helped = True if (row[4] == 0) else False
		location = row[5]
		duration = int(row[6])
		helpedBy = row[7]
		return entry(name, course, location, helped, duration, helpedBy, eid)

	def add(self, obj):
		self.queue.append(obj)
		#add to db
		with self.conn:
			cur = self.conn.cursor()
			sql = 'insert into ' + self.tableName + ' values (' + self.objToDB(obj) + ');'
			cur.execute(sql)
			self.conn.commit()

	def objToDB(self, obj):
		# should be in tableFormat with (x,x,'yyz') etc
		eid = obj.eid
		name = obj.name
		subtime = obj.subTime
		course = obj.course
		helped = str(0) if obj.helped else str(1)
		location = obj.location
		duration = str(obj.duration)
		helpedBy = obj.helpedBy
		return self.wrapString(eid) + ', ' + self.wrapString(name) + ', ' + self.wrapString(subtime) + ', ' + self.wrapString(course) + ', ' + helped + ', '+ self.wrapString(location) + ', ' + duration + ', ' + self.wrapString(helpedBy)

	def wrapString(self, s):
		return '\'' + s + '\''

	def modify(self, obj):
		if self.remove(obj.eid) == True:
			sql = "delete from " + self.tableName + " * where eid = " + self.wrapString(obj.eid) + ";"
			with self.conn:
				cur = self.conn.cursor()
				cur.execute(sql)
				self.conn.commit()
			self.add(obj)
			return obj
		return "EID not found in queue"

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