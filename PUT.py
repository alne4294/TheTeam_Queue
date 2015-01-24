

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
