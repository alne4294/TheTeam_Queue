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