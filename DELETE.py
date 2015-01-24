#/remove/id/#

@app.route('/api/1.0/queue/eid/<int:eid>')
def removeById(id):
	isTrue = True
	entryList.remove(eid)
	return, format(isTrue, eid)

