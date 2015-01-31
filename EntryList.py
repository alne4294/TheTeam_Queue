import sqlite3
from collections import deque
from Entry import entry

class EntryList:
	databaseFilename = "./entries.sqlite3"
	tableName = "Entries"
	tableFormat = "(eid TEXT PRIMARY KEY, name TEXT, subtime TEXT, course TEXT, helped INT, location TEXT, duration INT, helpedby TEXT)"

	def __init__(self, obj=None, testing=False):
		self.conn = sqlite3.connect(self.databaseFilename, check_same_thread=False)
		self.queue = []
		with self.conn:
			cur = self.conn.cursor()
			drop = "drop table if exists " + self.tableName
			if testing:
				cur.execute(drop)
			self.testing = testing
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
		something = entry(jsonStr=obj)
		n = 0
		for item in self.queue:
			if item.eid == something.eid:
				self.queue[n] = something
			n+=1
			return something
		return "EID not found in queue"

	def remove(self, eid, duration = -1):
		for item in self.queue:
			if item.eid == eid:
				if duration != -1:
					item.duration = duration
				self.queue.remove(item)
				return True
		return False # Wasn't found

	# def deleteFromDB(self, uuid):
	# 	query = "delete from " + self.tableName + " * where eid = " + self.wrapString(uuid) + ";"
	# 	with self.conn:
	# 		cur = self.conn.cursor()
	# 		cur.execute(query)
	# 		self.conn.commit()

	def clearDb(self):
		with self.conn:
			cur = self.conn.cursor()
			drop = "drop table if exists " + self.tableName
			cur.execute(drop)
			self.conn.commit()

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