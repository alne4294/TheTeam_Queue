import json as j
from datetime import datetime
from uuid import uuid4


class entry:
	def __init__(self, name = None, course = None, location = None, helped = False, duration = -1, helpedBy = "Not Helped", jsonStr = None):
		if jsonStr == None:
			self.name = str(name)
			self.eid = str(uuid4())
			self.subTime = str(datetime.now())
			self.course = str(course)
			self.helped = helped
			self.location = str(location)
			self.duration = duration
			self.helpedBy = str(helpedBy)
		elif jsonStr:
			self.name = jsonStr['name']
			self.eid = jsonStr['eid']
			self.subTime = jsonStr['subTime']
			self.course = jsonStr['course']
			self.helped = jsonStr['helped']
			self.location = jsonStr['location']
			self.duration = jsonStr['duration']
			self.helpedBy = jsonStr['helpedBy']



	def format(self):
		return j.JSONEncoder().encode({"name": self.name,"eid": self.eid, "subTime":self.subTime,
					   "course": self.course, "helped": self.helped, "location": self.location,
					   "duration": self.duration, "helpedBy": self.helpedBy})
        def __str__(self):
                return '{"name":"' + str(self.name) + '", "eid":"' + str(self.eid) + '", "subTime":"' + str(self.subTime) + '", "course":"'\
                        + str(self.course) + '", "helped":"' + str(self.helped) + '", "location":"' + str(self.location) + '", "duration":"'\
                        + str(self.duration) + '", "helpedBy":"' + str(self.helpedBy) + '"}'


