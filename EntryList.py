import sqlite3
from collections import deque

class EntryList:
	databaseFilename = "./entries.sqlite3"
	tableName = "Entries"
	tableFormat = "(eid TEXT PRIMARY KEY, subtime TEXT, course TEXT, helped TEXT, location TEXT, duration INT, helpedby TEXT)"

	def __init__(self, obj=None):
		self.conn = sqlite3.connect(databaseFilename)
		with cur = conn.cursor():
			sql = 'create table if not exists ' + tableName + tableFormat
			cur.execute(sql)
			cur.commit()
		self.queue = deque()

	def add(self, obj):
		self.queue.append(obj)
		#add to db
		sql = 'insert into ' + tableName + ' values '

	def objToDB(obj):
		# should be in tableFormat with (x,x,'yyz') etc
		eid = str(obj.eid)
		subtime = str(obj.subTime)
		course = obj.course
		helped = str(obj.helped)
		location = obj.location
		duration = obj.duration
		helpedBy = obj.helpedBy
		return

	@staticmethod
	def __wrapString(s):
		return '\'' + s + '\''

	def modify(self, obj):
		for item in self.queue:
			if item.eid == obj.eid:
				item = obj
				return obj

	def remove(self, eid, duration):
		for item in self.queue:
			if item.eid == eid:
				item.duration = duration
				self.__updateDB()
				self.queue(item)
				return True
		return False # Wasn't found

	def getById(self, x):
		for item in self.queue:
			if item.eid == x:
				return item
		return None

	def getByPos(self, x):
		if x > len(o) or x < 0:
			return None
		return self.queue[x]

	def getAll(self):
		return self.queue

	def __updateDB(self):
		# called every time queue is changed
		return None
