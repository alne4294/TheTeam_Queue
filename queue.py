#Handles REST requests from server for a queueing system

from datetime import datetime
from EntryList import EntryList
from flask import Flask
import collections

app = Flask(__name__)
entryList = EntryList()

#==========================================================
#GET

#/queue
@app.route('/api/1.0/queue/pos/<int:pos>')
def getByPos(pos):
	entryList.getByPos(pos)
	return format_response(True, pos)

#/queue/id/#
@app.route('/api/1.0/queue/id/<string:uuid>')
def getById(uuid):
	entryList.getById(uuid)
	return format(True, uuid)

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
	return format(True, uuid)

#==========================================================
#POST

#/enqueue
@app.route('/api/1.0/enqueue', methods = ['POST'])
def create():
    entryData = request.json
    newEntry = entry(name = entryData.name, course = entryData.course, location = entryData.location)
    entryList.add(newEntry)
    return format_response(True, newEntry)

#==========================================================
#PUT

#/modify/id/#
@app.route('/api/1.0/modify/id/<string:uuid>', methods = ['PUT'])
def modify(uuid):
    entryData = request.json
    modifiedData = entry(entryData)
    if entry.eid != UUID(uuid):
        return format_response(False, "The modified entry does not match the provided id")
    entryList.modify(modifiedData)
    return format_response(True, entryList.getById(modifiedData.eid))

#/dequeue/id/#
@app.route('/api/1.0/dequeue/id/<string:uuid>', methods = ['PUT'])
def dequeue(uuid):
    entryData = request.json
    modifiedData = entry(entryData)
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