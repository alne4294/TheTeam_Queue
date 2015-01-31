from uuid import uuid4
from datetime import datetime
import json as j

class entry:
    def __init__(self, name = "", course = "", location = "", helped = False, duration = -1, helpedBy = "Not Helped", eid = None, jsonStr=None):
        if jsonStr == None:
            self.name = str(name)
            self.eid = str(uuid4()) if eid == None else eid
            self.subTime = str(datetime.now())
            self.course = str(course)
            self.helped = helped
            self.location = str(location)
            self.duration = duration
            self.helpedBy = str(helpedBy)
        else:
            self.name = jsonStr['name']
            self.eid = jsonStr['eid']
            self.subTime = str(datetime.now())
            self.course = jsonStr['course']
            self.helped = helped
            self.location = jsonStr['location']
            self.duration = duration
            self.helpedBy = helpedBy

    def format(self):
        return {
            "name": self.name, 
            "eid": self.eid,
            "subTime":self.subTime,
            "course": self.course,
            "helped": self.helped,
            "location": self.location,
            "duration": self.duration,
            "helpedBy": self.helpedBy 
        }