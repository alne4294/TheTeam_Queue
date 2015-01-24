import sqlite3
import collections

class EntryList:
	databaseFilename = "./entries.sqlite3"
	tableName = "Entries"

	def __init__(self, obj=None):
		self.conn = sqlite3.connect('data.db')
		with cur = conn.cursor():
			
		self.queue = collections.deque()

	def add(self, obj):
		self.queue.append(obj)
		#add to db

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
