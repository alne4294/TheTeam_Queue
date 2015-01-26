#Handles REST requests from server for a queueing system

from datetime import datetime
from EntryList import EntryList
from flask import Flask, request
from collections import deque
import json as j
from uuid import uuid4


app = Flask(__name__)
entryList = EntryList()

#==========================================================
#Entry class

class entry:
    def __init__(self, name, course, location, helped = False, duration = -1, helpedBy = "Not Helped"):
        self.name = str(name)
        self.eid = str(uuid4())
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

#==========================================================
#Formats response to JSON

def format_response(success, obj):
    response = {"error": not success}
    if isinstance(obj, deque):
        data = "["
        for elt in obj:
            data += elt.format() + ","
            data += "]"
            response["data"] = data
    elif isinstance(obj, entry):
        response["data"] = obj.format()
    else:
        response["data"] = j.dumps(obj)
        return j.dumps(response)


#==========================================================
#GET

#/queue
@app.route('/api/1.0/queue/pos/<int:pos>')
def getByPos(pos):
    entry = entryList.getByPos(pos)
    isTrue = True
    if entry == None:
        isTrue = False
        entry = "No entry at position: " + pos
    return format_response(isTrue, entry)

#/queue/id/#
@app.route('/api/1.0/queue/id/<string:uuid>')
def getById(uuid):
    entry = entryList.getById(uuid)
    isTrue = True
    if entry == None:
        isTrue = False
        entry = "No entry at ID: " + uuid
    return format_response(isTrue, entry)

#/queue/pos/#
@app.route('/api/1.0/queue')
def getQueue():
    entries = entryList.getAll()
    return format_response(True, entries)

#==========================================================
#DELETE

#/remove/id/#
@app.route('/api/1.0/queue/id/<string:uuid>', methods = ['DELETE'])
def removeById(uuid):
    entryList.remove(uuid)
    return format_response(True, uuid)

#==========================================================
#POST

#/enqueue
@app.route('/api/1.0/enqueue', methods = ['POST'])
def create():
    entryData = request.get_json(force=True)
    newEntry = entry(name = entryData['name'], course = entryData['course'], location = entryData['location'])
    entryList.add(newEntry)
    return format_response(True, newEntry)

#==========================================================
#PUT

#/modify/id/#
@app.route('/api/1.0/modify/id/<string:uuid>', methods = ['PUT'])
def modify(uuid):
    entryData = request.get_json(force=True)
    modifiedData = entry(jsonstr = entryData)

    if entry.eid != UUID(uuid):
        return format_response(False, "The modified entry does not match the provided id")
    entryList.modify(modifiedData)
    return format_response(True, entryList.getById(modifiedData.eid))

#/dequeue/id/#
@app.route('/api/1.0/dequeue/id/<string:uuid>', methods = ['PUT'])
def dequeue(uuid):
    entryData = request.get_json(force=True)
    modifiedData = entry(jsonstr=entryData)
    if entry.eid != UUID(uuid):
        return format_response(False, "The modified entry does not match the provided id")
        success = entryList.remove(modifiedData)
        if success:
            return format_response(success, modifiedData)
        else:
            return format_response(success, "The entry was not dequeued successfully")

if __name__ == '__main__':
    app.debug = True
    app.run()
