#Handles REST requests from server for a queueing system

from datetime import datetime
from entry import entry
from EntryList import EntryList
from flask import Flask, request, jsonify
from collections import deque
import json as j
from uuid import uuid4


app = Flask(__name__)
entryList = EntryList()

#==========================================================
#Formats response to JSON

def format_response(success, obj):
    response = {"error": not success}
    if isinstance(obj, deque):
        data = []
        for elt in obj:
            data.append(elt.format())
        response["data"] = data
    elif isinstance(obj, entry):
        response["data"] = obj.format()
    else:
        response["data"] = obj
    return jsonify(**response)


#==========================================================
#GET


@app.route('/api/1.0/queue/pos/<int:pos>')
def getByPos(pos):
    if request.method == 'GET':
        entry = entryList.getByPos(pos)
        isTrue = True
        if entry == None:
            isTrue = False
            entry = "No entry at position: " + pos
        return format_response(isTrue, entry)
    else:
        return format_response(False, "Need a GET request at this endpoint")

#/queue/id/#
@app.route('/api/1.0/queue/id/<string:uuid>')
def getById(uuid):
    if request.method == 'GET':
        entry = entryList.getById(uuid)
        isTrue = True
        if entry == None:
            isTrue = False
            entry = "No entry at ID: " + uuid
        return format_response(isTrue, entry)
    else:
        return format_response(False, "Need a GET request at this endpoint")

#/queue
@app.route('/api/1.0/queue', methods = ['GET','POST'])
def getPostQueue():
    if request.method == 'GET':
        entries = entryList.getAll()
        return format_response(True, entries)
    elif request.method == 'POST':
        entryData = request.get_json(force=True)
        newEntry = entry(name = entryData['name'], course = entryData['course'], location = entryData['location'])
        entryList.add(newEntry)
        return format_response(True, newEntry)
    else:
        return format_response(False, "Need a GET/POST request at this endpoint")

#==========================================================
#DELETE

#/remove/id/#
@app.route('/api/1.0/queue/id/<string:uuid>', methods = ['DELETE'])
def removeById(uuid):
    entryList.remove(uuid)
    return format_response(True, uuid)


#==========================================================
#PUT

#/modify/id/#
@app.route('/api/1.0/modify/id/<string:uuid>', methods = ['PUT'])
def modify(uuid):
    entryData = request.get_json(force=True)
    modifiedData = entry(jsonStr=entryData)

    if entry.eid != UUID(uuid):
        return format_response(False, "The modified entry does not match the provided id")
    entryList.modify(modifiedData)
    return format_response(True, entryList.getById(modifiedData.eid))

#/dequeue/id/#
@app.route('/api/1.0/dequeue/id/<string:uuid>', methods = ['PUT'])
def dequeue(uuid):
    entryData = request.get_json(force=True)
    modifiedData = entry(jsonStr=entryData)
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
