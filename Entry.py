from uuid import uuid4
from datetime import datetime
import json as j

class entry:
    def __init__(self, name, course, location, helped = False, duration = -1, helpedBy = "Not Helped", eid = None):
        self.name = str(name)
        self.eid = str(uuid4()) if eid == None else eid
        self.subTime = str(datetime.now())
        self.course = str(course)
        self.helped = helped
        self.location = str(location)
        self.duration = duration
        self.helpedBy = str(helpedBy)

    # def __init__(self, json):
    #     self.name = json['name']
    #     self.eid = json['eid']
    #     self.subTime = json['subTime']
    #     self.course = json['course']
    #     self.helped = json['helped']
    #     self.location = json['location']
    #     self.duration = json['duration']
    #     self.helpedBy = json['helpedBy']


    def format(self):
        return j.JSONEncoder().encode({"name": self.name,"eid": self.eid, "subTime":self.subTime,
         "course": self.course, "helped": self.helped, "location": self.location,
         "duration": self.duration, "helpedBy": self.helpedBy})