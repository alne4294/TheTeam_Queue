from datetime import datetime

@app.route('/api/1.0/enqueue', methods = ['POST'])
def create():
    entryData = request.json
    newEntry = entry(name = entryData.name, course = entryData.course, location = entryData.location)
    entryList.add(newEntry)
    return format_response(true, newEntry)
