import sqlite3
import collections

class EntryList:

	def __init__(self, obj=None):
		self.conn = sqlite3.connect('data.db')
		self.c = conn.cursor()
		self.queue = collections.deque()

	def add(self, obj):
		self.queue.append(obj)
		#add to db

	def modify(self, obj):
		#find, modify, return

	def remove(self, eid, duration):
		for item in self.queue:
			if item.eid == eid:
				item.duration = duration
				self.__updateDB()
				self.queue(item)

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
