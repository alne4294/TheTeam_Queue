
from datetime import datetime

#==========================================================
#GET

#/queue
#/queue/id/#
#/queue/pos/#

@app.route('/api/1.0/queue/pos/<int:pos>')
def getByPos(pos):
	isTrue = True
	entryList.getByPos(pos)
	return, format_response(isTrue, pos)

@app.route('/api/1.0/queue/eid/<int:eid>')
def getById(id):
	isTrue = True
	entryList.getById(eid)
	return, format(isTrue, eid)

@app.route('/api/1.0/queue')
def getQueue():
	isTrue = True
	entryList.getAll()
	return, format_response(isTrue, x)

#==========================================================
#DELETE

#/remove/id/#

@app.route('/api/1.0/queue/eid/<int:eid>')
def removeById(eid):
	isTrue = True
	entryList.remove(eid)
	return, format(isTrue, eid)

#==========================================================
#POST

@app.route('/api/1.0/enqueue', methods = ['POST'])
def create():
    isTrue = True
    entryData = request.json
    newEntry = entry(name = entryData.name, course = entryData.course, location = entryData.location)
    entryList.add(newEntry)
    return format_response(isTrue, newEntry)

#==========================================================
#PUT

@app.route('api/1.0/modify/id/<string>:uuid')
def modify():
    entryData = request.json
    modifiedData = entry(entryData)
    if entry.eid != UUID(uuid):
        return format_response(false, "The modified entry does not match the provided id")
    entryList.modify(modifiedData)
    return format_response(true, entryList.getById(modifiedData.eid))

@app.route('api/1.0/dequeue/id/<string:uuid>')
def dequeue():
    entryData = request.json
    modifiedData = entry(entryData)
    if entry.eid != UUID(uuid):
        return format_response(false, "The modified entry does not match the provided id")
    success = entryList.remove(modifiedData)
    if success:
        return format_response(success, modifiedData)
    else:
        return format_response(success, "The entry was not dequeued successfully")
